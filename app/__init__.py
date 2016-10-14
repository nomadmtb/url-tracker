from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize our application with config file
app = Flask(__name__)
app.config.from_object('config')

# Initialize our database with SQLAlchemy
db = SQLAlchemy(app)

# Setup general error handlers (400, 500)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500

from app.url_tracker.controllers import url_tracker as tracker_module
from app.url_tracker.helpers import datetime_filter

# Apply our blueprint
app.register_blueprint(tracker_module)

# Register our Jinja2 filter(s)
app.jinja_env.filters['datetime'] = datetime_filter

db.create_all()
