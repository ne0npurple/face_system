import os
import form
import random
import json
import lib.common_functions as utils

from mlwdb import databs
from flask_session import Session
from flask import request, Flask, session, redirect, render_template, send_from_directory

SESSION_TYPE = 'filesystem'
app=Flask(__name__)
app.secret_key = 'Df4:Vj Mm`L"iLV#|{"I!RY<2F+)L-wz.sm("&H_,\(1FpG{HJ^lH"E$qsDpz`$Omu,bwi#J\OB7:F:HR*~?Z*9U} Dr]5bHeZ~VrDm7Ro(TQGZaYbNsoT."[&/>>5%Q'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['WTF_CSRF_ENABLED'] = False

sess = Session()
sess.init_app(app)

@app.route("/", methods=["GET"])
def main():
    if 'id' in session:
        return redirect("/index")
    return utils.my_render_template("homepage.html")

@app.route("/login", methods=["POST"])
def login():
    if 'id' in session:
        return redirect("/index")
    worker_id = request.form.get("worker_id", None)
    password = request.form.get("password", None)
    if worker_id is None or password is None:
        return redirect("/")
    password = utils.password_hash(password)
    print(password)
    result = databs().fetch("""
            select student_id as id, name from students where password=%s and student_id=%s and verified=1
            union
            select teacher_id as id, name from teachers where password=%s and teacher_id=%s
            union
            select worker_id as id, name as name from administrators where password=%s and worker_id=%s
            """, [password, worker_id, password, worker_id, password, worker_id])
    if len(result) != 1:
        return redirect("/?error_msg=login failed")

    session['username'] = result[0][1]
    session['id'] = result[0][0]
    return redirect("/index")

@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect("/")

@app.route("/index", methods=["GET"])
def index():
    if 'id' not in session:
        return redirect("/")
    return utils.my_render_template("index.html")

@app.route("/test", methods=["GET"])
def aaaa():
    if len(databs().fetch("select * from students where student_id='" + request.args['account'] + "' and password='" + request.args['password'] + "'")) > 0:
        return "select * from students where student_id='" + request.args['account'] + "' and password='" + request.args['password'] + "'" + "success"
    return "select * from students where student_id='" + request.args['account'] + "' and password='" + request.args['password'] + "'"+ "try again"

url = "127.0.0.1:8080/verify?code=0.501746177926953&worker_id=123456&type=admin"
@app.route("/verify", methods=["GET"])
def verify():
    if 'code' in request.args and 'worker_id' in request.args and 'type' in request.args:
        account=None
        update_sql = None
        if request.args['type'] == "admin":
            account = databs().fetch('''
                select worker_id as id, vkey as name from administrators where worker_id=%s
            ''', [request.args['worker_id']])
            update_sql = "update administrators set verified=1 where worker_id=%s"
        elif request.args['type'] == "student":
            account = databs().fetch('''
                select student_id as id, vkey from students where student_id=%s
            ''', [request.args['worker_id']])
            update_sql = "update students set activated=1 where student_id=%s"
        elif request.args['type'] == "teacher":
            account = databs().fetch('''
                select teacher_id as id, vkey from teachers where teacher_id=%s
            ''', [request.args['worker_id']])
            update_sql = "update teachers set activated=1 where teacher_id=%s"
        if not account == None:
            print(account)
            print(account[0][1], request.args['code'])
            if account[0][1] == request.args['code']:
                print("ADASDSAD")
                databs().commit(update_sql, request.args['worker_id'])
    return redirect("/")

@app.route("/register", methods=["GET"])
def register_get():
    if 'id' in session:
        return redirect("/index")
    return utils.my_render_template("register.html")

@app.route("/register", methods=["POST"])
def register_post():
    if 'id' in session:
        return redirect("/index")
    submit_form = form.regist_page()
    if submit_form.validate_on_submit():
        name = submit_form.name.data
        worker_id = submit_form.worker_id.data
        email = submit_form.email.data
        password = submit_form.password.data
        account_type = submit_form.account_type.data

        if account_type == "students":
            field = "(`name`, `student_id`, `email`, `password`, `vkey`, `gender`, `reg_time`, `class`, `verified`)"
            value = "(%s, %s, %s, %s, %s, 'Unknow', NOW(), `Not Specified`, '0')"
        elif account_type == "teachers":
            field = "(`name`, `teacher_id`, `email`, `password`, `vkey`, `dept`, `reg_time`, `activated`)"
            value = "(%s, %s, %s, %s, %s, 'Unknow', NOW(), '0')"
        elif account_type == "administrators":
            field="(`name`, `worker_id`, `email`, `password`, `vkey`, `verified`)"
            value = "(%s, %s, %s, %s, %s, '0')"
        vkey = utils.password_hash(str(random.random()))
        utils.send_email(email, "verify your account",
                "127.0.0.1:8080/verify?code=%s&worker_id=%s&type=admin" % (vkey, worker_id))
        sql = "INSERT INTO `%s` %s VALUES %s;" % (account_type, field, value)
        print(sql)
        databs().commit(sql, [name, worker_id, email, utils.password_hash(password), vkey])
        return redirect('/')
    else:
        print(submit_form.name.errors)
        print(submit_form.worker_id.errors)
        print(submit_form.email.errors)
        print(submit_form.password.errors)
        print(submit_form.errors.items())
        return "input error"

@app.route("/assets/img/<path:path>", methods=["GET"])
def send_img(path):
    return send_from_directory("./assets/img", path)

@app.route("/assets/js/<path:path>", methods=["GET"])
def send_js(path):
    return send_from_directory("./assets/js", path)

@app.route("/assets/css/<path:path>", methods=["GET"])
def send_css(path):
    return send_from_directory("./assets/css", path)

app.run(port=8080, debug=True)
