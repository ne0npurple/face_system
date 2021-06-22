from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, IntegerField
from wtforms.validators import Required,InputRequired,Length,NumberRange,EqualTo,Optional

class regist_page(FlaskForm):
    name = StringField("name", validators=[InputRequired(), Length(max=30)])
    account_type = RadioField("account_type", validators=[InputRequired()],
                              choices=[
                                  ("students", "students"),
                                  ("teachers", "teachers"),
                                  ("administrators", "administrators")
                              ])
    worker_id = StringField("worker_id", validators=[InputRequired(), Length(max=10)])
    email = StringField("email", validators=[InputRequired()])
    password = StringField("password", validators=[InputRequired()])
    password_conf = StringField()


class courses(FlaskForm):
    course_name = StringField("course_name", validators=[InputRequired()])
    course_code = StringField("course_code", validators=[InputRequired(), Length(max=4)])
    credit = StringField("credit", validators=[InputRequired(), Length(max=1)])
    hours = StringField("hours", validators=[InputRequired(), Length(max=1)])

class updatecourses(FlaskForm):
    course_id = IntegerField("course_id", validators=[InputRequired()])
    course_name = StringField("course_name", validators=[InputRequired()])
    course_code = StringField("course_code", validators=[InputRequired(), Length(max=4)])
    credit = StringField("credit", validators=[InputRequired(), Length(max=1)])
    hours = StringField("hours", validators=[InputRequired(), Length(max=1)])

class courses_list(FlaskForm):
    course_id = IntegerField("course_id", validators=[InputRequired()])
    teacher_id = StringField("teacher_id", validators=[InputRequired()])
    day = StringField("day", validators=[InputRequired()])
    time_start = StringField("time_start", validators=[InputRequired()])
    time_end = StringField("time_end", validators=[InputRequired()])

class updatecourseslist(FlaskForm):
    serial = IntegerField("serial", validators=[InputRequired()])
    course_id = IntegerField("course_id", validators=[InputRequired()])
    teacher_id = StringField("teacher_id", validators=[InputRequired()])
    day = StringField("day", validators=[InputRequired()])
    time_start = StringField("time_start", validators=[InputRequired()])
    time_end = StringField("time_end", validators=[InputRequired()])

class studentlist(FlaskForm):
    student_id = StringField("student_id", validators=[InputRequired()])
    name = StringField("name", validators=[InputRequired()])
    grade = StringField("grade", validators=[InputRequired()])
    gender = StringField("gender", validators=[InputRequired()])
    email = StringField("email", validators=[InputRequired()])
    reg_time = StringField("reg_time", validators=[InputRequired()])

class updatestudentlist(FlaskForm):
    student_id = StringField("student_id", validators=[InputRequired()])
    name = StringField("name", validators=[InputRequired()])
    grade = StringField("grade", validators=[InputRequired()])
    gender = StringField("gender", validators=[InputRequired()])
    email = StringField("email", validators=[InputRequired()])
    reg_time = StringField("reg_time", validators=[InputRequired()])

class teacherlist(FlaskForm):
    teacher_id = StringField("teacher_id", validators=[InputRequired()])
    name = StringField("name", validators=[InputRequired()])
    email = StringField("email", validators=[InputRequired()])
    reg_time = StringField("reg_time", validators=[InputRequired()])

class updateteacherlist(FlaskForm):
    teacher_id = StringField("teacher_id", validators=[InputRequired()])
    name = StringField("name", validators=[InputRequired()])
    email = StringField("email", validators=[InputRequired()])
    reg_time = StringField("reg_time", validators=[InputRequired()])

class studentscourses(FlaskForm):
    student_id = StringField("student_id", validators=[InputRequired()])
    course_id = IntegerField("course_id", validators=[InputRequired()])

class updatestudentscourses(FlaskForm):
    serial = IntegerField("serial", validators=[InputRequired()])
    student_id = StringField("student_id", validators=[InputRequired()])
    course_id = IntegerField("course_id", validators=[InputRequired()])

class teacherscourses(FlaskForm):
    teacher_id = StringField("teacher_id", validators=[InputRequired()])
    course_id = IntegerField("course_id", validators=[InputRequired()])

class updateteacherscourses(FlaskForm):
    serial = IntegerField("serial", validators=[InputRequired()])
    teacher_id = StringField("teacher_id", validators=[InputRequired()])
    course_id = IntegerField("course_id", validators=[InputRequired()])

class updatestudentsprofile(FlaskForm):
    student_id = StringField("student_id", validators=[InputRequired()])
    name = StringField("name", validators=[InputRequired()])
    grade = StringField("grade", validators=[InputRequired()])
    gender = StringField("gender", validators=[InputRequired()])
    email = StringField("email", validators=[InputRequired()])


class updateteachersprofile(FlaskForm):
    teacher_id = StringField("teacher_id", validators=[InputRequired()])
    name = StringField("name", validators=[InputRequired()])
    email = StringField("email", validators=[InputRequired()])

class updateadminsprofile(FlaskForm):
    worker_id = StringField("worker_id", validators=[InputRequired()])
    name = StringField("name", validators=[InputRequired()])
    email = StringField("email", validators=[InputRequired()])

class insertattendance(FlaskForm):
    student_id = StringField("student_id", validators=[InputRequired()])
    course_id = IntegerField("course_id", validators=[InputRequired()])
