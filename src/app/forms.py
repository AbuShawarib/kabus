from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email


class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[
        InputRequired('Please enter your message.')])
    name = StringField('Name', validators=[
        InputRequired('Please enter your name.')])
    email = StringField('Email', validators=[
        InputRequired('Please enter your email address.'),
        Email('This field requires a valid email address')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Send Message')
