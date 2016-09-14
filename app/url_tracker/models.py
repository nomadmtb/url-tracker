# Models for the Application
from app import db
import random, string


def generate_key(length=10):
    generated_key = ''

    for i in range(length):

        generated_key += random.choice(
            string.lowercase + string.uppercase + string.digits
        )

    return generated_key


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Target(Base):

    __tablename__ = 'url_tracker__target'

    destination = db.Column(db.String(2083), nullable=False)
    ip_address = db.Column(db.String(250), nullable=True)
    tracking_key = db.Column(db.String(250), nullable=True)
    manage_key = db.Column(db.String(250), nullable=True)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, ip=None):

        self.ip_address = ip
        self.tracking_key = generate_key(length=15)
        self.manage_key = generate_key(length=15)

    def __repr__(self):

        return '<Target {0}>'.format(self.tracking_key)
