# Forms for the Application...
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import URL, Required

class CreateTargetForm(Form):
    destination = TextField('URL To Track', [
        URL(), Required(message='Enter a URL to track')
    ])
