# Controller methods for the Application
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.url_tracker.forms import CreateTargetForm
from app.url_tracker.models import Target

url_tracker = Blueprint('url', __name__, url_prefix='/url')

@url_tracker.route('', methods=['GET', 'POST'])
def create():

    create_form = CreateTargetForm(request.form)

    if create_form.validate_on_submit():
        pass

    return render_template('url_tracker/create.html', form=create_form)
