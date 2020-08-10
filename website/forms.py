from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, ValidationError
from website.models import Link

class LinkForm(FlaskForm):
    link = StringField('Custom URL Ending', validators=[DataRequired()])
    url = StringField('URL to Redirect To', validators=[DataRequired()])
    title = StringField('Site Title', validators=[DataRequired()])
    name = StringField('Site Name', validators=[DataRequired()])
    desc = StringField('Description', validators=[DataRequired()])
    image = StringField('Link to Image', validators=[DataRequired()])    
    submit = SubmitField('Submit')
    
    def validate_link(self, link):
        goodlink = link.data.replace(' ','-')
        goodlink = goodlink.replace('/','_')
        goodlink = goodlink.replace(':','-')
        goodlink = goodlink.replace('.','-')
        goodlink = goodlink.replace('?','-')
        goodlink = goodlink.replace(',','-')

        alink = Link.query.filter_by(link=goodlink).first()
        if alink:
            raise ValidationError('That link is already taken')
