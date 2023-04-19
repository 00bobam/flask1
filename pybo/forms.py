from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username =  StringField("아이디",
                            validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField("비밀번호",
                            validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField("접속")