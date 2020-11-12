"""Forms for Cupcake"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional, URL


class AddCupcakeForm(FlaskForm):
    """Form for adding cupcakes."""

    flavour = StringField("Cupcake Flavour", 
                        validators=[InputRequired()])
    size = StringField("Size", 
                        validators=[InputRequired()])
    rating = FloatField("Rating", 
                        validators=[InputRequired()])
    image = StringField("Image URL", 
                        validators=[Optional(), URL(require_tld=False)])
