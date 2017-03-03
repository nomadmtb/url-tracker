# Controller methods for the Application
from flask import (
    Blueprint, request, render_template, flash, redirect,
    jsonify, current_app, make_response, send_from_directory, abort
)

from app import db
from app.url_tracker.forms import CreateTargetForm
from app.url_tracker.models import Target, Click
from app.url_tracker.helpers import generate_trend, generate_csvdata
from datetime import datetime
import requests, json
import pdb

url_tracker = Blueprint('root', __name__)

# Create()
# In this method we will be using the validated url from the CreateTargetForm
# to create a new instance of the Target class. If the form validates then the
# Tracker instance is saved to the database, else the form gets re-rendered with
# the appropriate errors.
#
@url_tracker.route('/', methods=['GET', 'POST'])
def create():

    # Create instance of the form from the request data.
    create_form = CreateTargetForm(request.form)

    # Check to see if the form passes validation. Just checks for a valid URL.
    if create_form.validate_on_submit():

        try:
            resp = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                params = {
                    'secret': current_app.config.get('RECAPCHA_SECRET'),
                    'response': request.form['g-recaptcha-response'],
                }
            )
        except:
            return redirect('/')

        if json.loads(resp.text)['success'] is False:
            return redirect('/')

        # We will attempt to generate a unique pair of keys 15 times at max.
        target_to_create = None
        for i in range(15):

            # Create the new instance of the Target class with the validated
            # data.
            new_target = Target(
                ip = request.remote_addr,
                dest_url = create_form.destination.data,
            )

            # Now we can validate the keys.
            existing_targets = Target.query.filter(
                db.or_(
                    Target.tracking_key == new_target.manage_key,
                    Target.manage_key == new_target.tracking_key
                )
            ).all()

            # If there are not matches in the DB already. Safe to create a new
            # Target object.
            if not existing_targets:
                target_to_create = new_target
                # We have a valid Target. Break out to save.
                break

        if target_to_create:

            # Save the new item to the database.
            db.session.add(new_target)
            db.session.commit()

            # Redirect to the manage url for the Target.
            return redirect('/u/{0}'.format(new_target.manage_key))

        else:

            # Return to the create page for a retry.
            return redirect('/')


    # Render the view with the form data.
    return render_template('url_tracker/create.html', form=create_form,
        recapcha_key=current_app.config.get('RECAPCHA_KEY')
    )


# Stats()
# This method will simply render the stats page that will show the click data
# across all tracked links.
#
@url_tracker.route('/stats', methods=['GET'])
def stats():

    return render_template(
        'url_tracker/stats.html',
        HOSTNAME=current_app.config['SERVERNAME']
    )


# View()
# In this method the code will query for the appropriate Target from the db and
# render the view page. If there is no matching Target a 404 will be raised.
#
@url_tracker.route('/u/<manage_key_param>', methods=['GET'])
def view(manage_key_param):

    # Grab the Target using the manage_key.
    selected_target = Target.query.filter_by(manage_key=manage_key_param).first()

    if selected_target:

        return render_template(
            'url_tracker/view.html',
            target=selected_target,
            click_count=selected_target.clicks.count(),
            HOSTNAME=current_app.config['SERVERNAME']
        )

    else:
        abort(404)

# GetCSV()
# In this method, the code will query for the appropriate Target and then build
# a csv file that will get returned to the user. The CSV will contain all of the
# click data for the target.
#
@url_tracker.route('/u/<manage_key_param>/click_data.csv', methods=['GET'])
def getcsv(manage_key_param):

    # Grab the Target using the manage_key.
    selected_target = Target.query.filter_by(manage_key=manage_key_param).first()

    if selected_target:

        clicks = selected_target.clicks.order_by(Click.date_created).all()

        # if there is click data return it. Else render 404.
        if clicks:

            csv_data = generate_csvdata(clicks)
            resp = make_response(csv_data)
            resp.headers['Content-Disposition'] = 'attachment; filename=mycsv.csv'
            resp.mimetype='text/csv'
            return resp

        # There is no clicks for this Target yet.
        else:
            abort(404)

    else:
        abort(404)


# Go()
# In this method the key url parameter is parsed out. This will attach to the
# Target object from the database. From here we can create a new instance of
# the Click class and attach it to the designated Target.
#
@url_tracker.route('/g/<target_key>', methods=['GET'])
def go(target_key):

    # If the key is supplied then proceed to lookup the Target.
    if target_key:

        # Pulling the attached_target from the database.
        attached_target = Target.query.filter_by(tracking_key=target_key).first()

        # Check if the attached_target was matched.
        if attached_target:

            # Create a new instance of our Click class.
            new_click = Click(
                ip = request.remote_addr,
                agent = str(request.user_agent),
                lang = str(request.accept_languages),
                ref = str(request.referrer)
            )

            # Save the assosicated Click instance to the target and commit.
            attached_target.clicks.append(new_click)
            db.session.add(attached_target)
            db.session.add(new_click)
            db.session.commit()

            # Redirect using the desired destination.
            return redirect(attached_target.destination)

        # Target was not in the database with a matching tracking_key.
        else:

            abourt(404)

    # Else, the key was not provided so render the 404 page.
    else:

        abourt(404)


# GetClicksForTarget()
# In this method we will be returning JSON data that represents all of the Click
# data for a particular Target. Will be returning Json for the Dynatable stuff
# on the front-end.
#
@url_tracker.route('/api/target_clicks/<manage_key>', methods=['GET'])
def getClicks(manage_key):

    if manage_key:

        attached_target = Target.query.filter_by(manage_key=manage_key).first()

        return jsonify( generate_trend( attached_target.clicks.order_by(Click.date_created).all()) )

    else:
        return abort(404)

# GetClickStats()
# This method will pull in all of the clicks from the entire application and
# return json data back to the requestor. Will populate our amCharts view via
# AJAX.
#
@url_tracker.route('/api/click_stats', methods=['GET'])
def getClickStats():

    # Load all clicks from the application...
    clicks = Click.query.order_by(Click.date_created).all()

    # Calculate the number of days to generate a trend for.
    num_days = (clicks[0].date_created - clicks[-1].date_created).days

    return jsonify( generate_trend( clicks ) )


# Robots()
# This method will simply render the robots.txt file back to the user.
#
@url_tracker.route('/robots.txt', methods=['GET'])
def robots():
    return send_from_directory(current_app.static_folder, 'robots.txt')
