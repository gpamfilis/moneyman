from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(Form):
    """
    This is the Login Form class. It has the Form as a parent. When used in templating the wtf automatically
    generates a Form just as seen when we navigate towards /login page.
    """
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegistrationForm(Form):
    """
    This is the Registration Form class. It has the Form as a parent. When used in templating the wtf automatically
    generates a Form just as seen when we navigate towards /register page.
    """
    email = StringField('Email', validators=[Required(),
                                             Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[Required(),
                                                   Length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
                                                          0,
                                                          'Usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(),
                                                     EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        """
        :param field:
        :return:
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        """
        :param field:
        :return:
        """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
