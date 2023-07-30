from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete, update, ForeignKey

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species= db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Text, default='yes')
