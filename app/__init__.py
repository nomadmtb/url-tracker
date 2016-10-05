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
app.register_blueprint(tracker_module)

db.create_all()
