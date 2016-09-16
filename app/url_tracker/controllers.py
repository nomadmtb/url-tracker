# Controller methods for the Application
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.url_tracker.forms import CreateTargetForm
from app.url_tracker.models import Target, Click
import pdb

url_tracker = Blueprint('root', __name__)

# Create()
# In this method we will be using the validated url from the CreateTargetForm
# to create a new instance of the Target class. If the form validates then the
# Tracker instance is saved to the database, else the form gets re-rendered with
# the appropriate errors.
@url_tracker.route('/', methods=['GET', 'POST'])
def create():

    # Create instance of the form from the request data.
    create_form = CreateTargetForm(request.form)

    # Check to see if the form passes validation. Just checks for a valid URL.
    if create_form.validate_on_submit():

        # Create the new instance of the Target class with the validated data.
        new_target = Target(
            ip = request.remote_addr,
            dest_url = create_form.destination.data,
        )

        # Save the new item to the database.
        db.session.add(new_target)
        db.session.commit()

        # Redirect to the manage url for the Target.
        return redirect('/u/{0}'.format(new_target.manage_key))

    # Render the view with the form data.
    return render_template('url_tracker/create.html', form=create_form)


# View()
# In this method the code will query for the appropriate Target from the db and
# render the view page. If there is no matching Target a 404 will be raised.
@url_tracker.route('/u/<manage_key_param>', methods=['GET'])
def view(manage_key_param):

    # Grab the Target using the manage_key.
    selected_target = Target.query.filter_by(manage_key=manage_key_param).first()

    if selected_target:
        return render_template('url_tracker/view.html', target=selected_target)
    else:
        return render_template('404.html'), 404


# Go()
# In this method the key url parameter is parsed out. This will attach to the
# Target object from the database. From here we can create a new instance of
# the Click class and attach it to the designated Target.
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

            return render_template('404.html'), 404

    # Else, the key was not provided so render the 404 page.
    else:

        return render_template('404.html'), 404
