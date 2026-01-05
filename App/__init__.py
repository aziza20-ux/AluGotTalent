import sqlite3
import os
from flask import Flask, render_template,session,g, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .routes.talentsAPI import talent_bp
from .routes.auth import auth_bp
from .routes.competitionsAPI import comp_bp
from .routes.sponsorAPI import sponsor_bp
from .routes.adminauth import admin_bp
from .routes.dashboardAPI import dash_bp
from .routes.user_viewAPI import userview_bp
from .routes.success import success_bp

# app.py

import sqlite3
from flask import Flask
from extentions import db, migrate, init_extensions
from App.models import user_model, talents, sponsor, student, successstroy
def create_app(test_config=None):
    app = Flask(__name__)
    # Load external PostgreSQL URL (Render)
    database_url = os.environ.get("DATABASE_URL")

    # Render sometimes provides postgres:// instead of postgresql://
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///my_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # secret_key = os.environ.get("SECRET_KEY", "testing")
    app.config['SECRET_KEY'] = "secret_key"

    init_extensions(app) 
    with app.app_context():
        db.create_all()


    @app.before_request
    def load_user_id():
        user_id = session.get('user_id')
        email= session.get('email')
        if user_id == None:
            g.user_id = None
            g.email = None
        else:
            g.user_id = user_id
            g.email = email
    @app.route('/')
    def index():
        return redirect(url_for('userview.successdisplayall'))
    
    app.register_blueprint(talent_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(comp_bp)
    app.register_blueprint(sponsor_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(dash_bp)
    app.register_blueprint(userview_bp)
    app.register_blueprint(success_bp)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app