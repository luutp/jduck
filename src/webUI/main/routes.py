#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
routes.py
Description:

Author: PhatLuu
Contact: tpluu2207@gmail.com
Created on: 2021/07/06
"""

#%%
# ================================IMPORT PACKAGES====================================

# Standard Packages
from os import system

# Visualization Packages
import cv2

# Utilities
from datetime import datetime

from flask import Blueprint
from flask import jsonify
from flask import render_template
from flask import request
from flask import Response
from flask import url_for
from flask_login import current_user

# Custom Packages
from jduck import system_info
from jduck.camera import CSICamera


main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("public/index.html")


@main.route("/get_system_info", methods=["GET"])
def get_system_info():
    timestamp = datetime.now().strftime("%y%m%d-%H%M%S")
    data = dict()
    data["ip_address"] = system_info.get_ip_address("eth0")
    data["cpu_usage"] = system_info.get_cpu_usage()
    data["disk_usage"] = system_info.get_disk_usage()
    data["timestamp"] = timestamp
    return jsonify(result=data)


@main.route("/about")
def about():
    return render_template("public/about.html", title="About")


@main.route("/video_feed")
def video_feed():
    return 0
    # cam = CSICamera()
    # return Response(
    #     cam.web_stream(), mimetype="multipart/x-mixed-replace; boundary=frame"
    # )
