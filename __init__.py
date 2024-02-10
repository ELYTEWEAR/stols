from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize the database
db = SQLAlchemy()

# Initialize the login manager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'

    db.init_app(app)
    login_manager.init_app(app)

    from .views import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    from .models import User  # This is to ensure our models are known to SQLAlchemy

    return app
