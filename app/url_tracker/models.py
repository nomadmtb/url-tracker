# Models for the Application
from app import db
import random, string


def generate_key(length=10):
    generated_key = ''

    for i in range(length):

        generated_key += random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits
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

    def __init__(self, ip=None, dest_url=None):

        self.ip_address = ip
        self.destination = dest_url
        self.tracking_key = generate_key(length=8)
        self.manage_key = generate_key(length=8)

    def to_dict(self):

        data = {
            'destination': self.destination,
            'ip_address': self.ip_address,
            'tracking_key': self.tracking_key,
            'manage_key': self.manage_key,
            'active': self.active,
        }

        return data

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

    def to_array(self):

        header = [
            'date_clicked',
            'ip_address',
            'user_agent',
            'language',
            'referrer'
        ]

        data = [
            self.date_created.strftime('%Y-%m-%d %H:%M:%S UTC'),
            self.ip_address,
            self.user_agent,
            self.language,
            self.referrer,
        ]

        return (header, data,)

    def to_dict(self):

        data = {
            'ip_address': self.ip_address,
            'user_agent': self.user_agent,
            'language': self.language,
            'referrer': self.referrer,
        }

        return data

    def __repr__(self):

        return '<Click {0}>'.format(self.ip_address)
