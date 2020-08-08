from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, ValidationError

class LinkForm(FlaskForm):
    link = StringField('Custom URL Ending', validators=[DataRequired()])
    url = StringField('URL to Redirect To', validators=[DataRequired()])
    title = StringField('Site Title', validators=[DataRequired()])
    name = StringField('Site Name', validators=[DataRequired()])
    desc = StringField('Description', validators=[DataRequired()])
    image = StringField('Link to Image', validators=[DataRequired()])    
    submit = SubmitField('Submit')

