#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
config.py
Description:

Author: PhatLuu
Contact: tpluu2207@gmail.com
Created on: 2021/07/06
"""

#%%
# ================================IMPORT PACKAGES====================================

# Standard Packages
import os
import sys

from dotenv import load_dotenv


script_dir = os.path.dirname(sys.argv[0])
dotenv_filepath = os.path.join(script_dir, ".env")
load_dotenv(dotenv_filepath)


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # Email
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")
    # Filepath
    APP_DIR = script_dir
    PROJECT_ROOT = os.path.dirname(APP_DIR)
    STATIC_DIR = os.path.join(APP_DIR, "static")
    UPLOAD_DIR = os.path.join(STATIC_DIR, "upload")
