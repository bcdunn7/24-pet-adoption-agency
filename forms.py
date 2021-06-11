from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.fields.html5 import URLField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class PetForm(FlaskForm):
    """Form for adding a new pet."""

    name = StringField("Pet Name",
                        validators = [InputRequired(message="Required")])

    species = StringField("Species",
                        validators = [InputRequired(message="Required"), AnyOf(values=["cat", "dog", "porcupine"], message="Must be cat, dog, or porcupine")])

    photo_url = URLField("Image URL",
                        validators = [Optional(), URL(message="Must be valid URL")])

    age = IntegerField("Age",
                        validators = [Optional(), NumberRange(min=0, max=30, message="Age must be 0-30")])

    notes = StringField("Notes",
                        validators = [Optional()])

    available = BooleanField("Available")