from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class ApiKeyInputForm(FlaskForm):
	apikey = StringField('Apikey', validators=[DataRequired()])
	submit = SubmitField('Request Data')
