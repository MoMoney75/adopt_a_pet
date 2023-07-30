from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange, URL, AnyOf 

class addPetForm(FlaskForm):
    """form for adding a new pet"""
    values_ = ['dog','cat', 'porcupine']

    name = StringField("Pet name", validators=[InputRequired(message="name is required")])
    species = StringField("Species", validators=[AnyOf(values_,message='valid species are dogs,cats and porcupines', values_formatter=None)])
    photo_url = StringField("Photo url")
    age = IntegerField("Age", validators=[NumberRange(0,30, message='Age must be between 0-30')])
    notes = StringField("Notes",validators=[InputRequired(message="Please provide some information about the pet")])
    
