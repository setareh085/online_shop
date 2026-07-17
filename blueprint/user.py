from flask import Blueprint, render_template, request, redirect
from flask_login import login_user
from passlib.hash import sha256_crypt
from extentions import db
from models.user import User
app = Blueprint("user", __name__)
@app.route('/user/login', methods=['GET', 'POST'])
def login():  # put application's code here
    if request.method == 'GET':
        return render_template("user/login.html")
    else:
        register = request.form.get("register", None)
        username = request.form['username']
        password = request.form['password']
        phone = request.form['phone']
        address = request.form['address']
        if register != None:
            user = User(username=username, password=sha256_crypt.encrypt(password), phone=phone, address=address)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect("/user/dashboard")
        return "done"