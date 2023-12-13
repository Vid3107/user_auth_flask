from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Coderistic' # encrypting sessions and cookies
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .models import User, Note

    app.register_blueprint(views)
    app.register_blueprint(auth)
    

    with app.app_context():
        create_database()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app=app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

def create_database():
    db_path = 'website/' + DB_NAME
    if not path.exists(db_path):
        try:
            db.create_all() 
            print('Database created!')
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    else:
        print('Database already exists!')