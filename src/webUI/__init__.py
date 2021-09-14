#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__init__.py
Description:

Author: PhatLuu
Contact: tpluu2207@gmail.com
Created on: 2021/07/06
"""

#%%
# ================================IMPORT PACKAGES====================================
from flask import Flask
from flask import render_template
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
bcrypt = Bcrypt()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail()


def page_not_found(e):
    return render_template("errors/404.html"), 404


def create_app():
    # App config
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Register Extension
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)

    # Custom Packages
    # Register apps
    with app.app_context():

        # Register blueprint
        # Custom Packages
        from webUI.main.routes import main

        app.register_blueprint(main)
        # app.register_blueprint(users)
        # Register error handlers
        app.register_error_handler(404, page_not_found)

        db.create_all()

        return app
