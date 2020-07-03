from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import Required,InputRequired,Length,NumberRange,EqualTo,Optional

class regist_page(FlaskForm):
    name = StringField("name", validators=[InputRequired(), Length(max=20)])
    worker_id = StringField("worker_id", validators=[InputRequired(), Length(max=10)])
    email = StringField("email", validators=[InputRequired()])
    password = StringField("password", validators=[InputRequired()])
    password_conf = StringField()
