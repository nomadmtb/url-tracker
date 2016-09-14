# Controller methods for the Application
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.url_tracker.forms import CreateTargetForm
from app.url_tracker.models import Target
import pdb

url_tracker = Blueprint('url', __name__, url_prefix='/url')

@url_tracker.route('', methods=['GET', 'POST'])
def create():

    create_form = CreateTargetForm(request.form)

    if create_form.validate_on_submit():
        print("Submitted form : {0}".format(create_form.destination))
        return redirect('go to view page with params')

    return render_template('url_tracker/create.html', form=create_form)

@url_tracker.route('/go')
def go():

    target_key = request.args.get('key')

    if target_key:
        attached_target = Target.query.filter_by(tracking_key=target_key)
    else:
        return render_template('404.html'), 404


    return render_template('url_tracker/create.html')
