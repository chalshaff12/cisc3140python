from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo

#form for api input
class ApiKeyInputForm(FlaskForm):
	apikey = StringField('Apikey', validators=[DataRequired()])
	apod = SubmitField('Picture of the Day')
	rover = SubmitField('Mars Rover Photos')
	epic = SubmitField('EPIC Photos')
