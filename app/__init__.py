from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.DevConfig')
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.url_tracker.controllers import url_tracker as tracker_module
app.register_blueprint(tracker_module)

db.create_all()
