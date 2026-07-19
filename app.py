from flask import Flask, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from blueprint.general import app as general
from blueprint.admin import app as admin
from blueprint.user import app as user
import config
import extentions
from flask_login import LoginManager

from models.user import User

app = Flask(__name__)
app.register_blueprint(general)

app.register_blueprint(admin)
app.register_blueprint(user)

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
extentions.db.init_app(app)
app.config['SECRET_KEY'] = config.SECRET_KEY
csrf = CSRFProtect(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()

@login_manager.unauthorized_handler
def unauthorized():
    flash("برای دسترسی به این صفحه وارد حساب کاربریتان شوید.")
    return redirect(url_for("user.login"))


with app.app_context():
    extentions.db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
