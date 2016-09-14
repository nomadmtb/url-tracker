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
    clicks = db.relationship('Click', backref='target', lazy='dynamic')

    def __init__(self, ip=None):

        self.ip_address = ip
        self.tracking_key = generate_key(length=15)
        self.manage_key = generate_key(length=15)

    def __repr__(self):

        return '<Target {0}>'.format(self.tracking_key)

class Click(Base):

    __tablename__ = 'url_tracker__click'

    ip_address = db.Column(db.String(250), nullable=True)
    user_agent = db.Column(db.String(250), nullable=True)
    language = db.Column(db.String(250), nullable=True)
    referrer = db.Column(db.String(500), nullable=True)
    target_id = db.Column(db.Integer, db.ForeignKey('url_tracker__target.id'))

    def __init__(self, ip=None, agent=None, lang=None, ref=None):

        self.ip_address = ip
        self.user_agent = agent
        self.language = lang
        self.referrer = ref

    def __repr__(self):

        return '<Click {0}>'.format(self.ip_address)
