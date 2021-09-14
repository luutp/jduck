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

# Visualization Packages
import cv2

from flask import Blueprint
from flask import render_template
from flask import request
from flask import Response
from flask import url_for
from flask_login import current_user

# Custom Packages
from jduck.camera import CSICamera


# # img_width, img_height = 1280, 720
# img_width, img_height = 480, 360


# def gstreamer_pipeline(
#     capture_width=img_width,
#     capture_height=img_height,
#     display_width=img_width,
#     display_height=img_height,
#     framerate=30,
#     flip_method=0,
# ):
#     return (
#         "nvarguscamerasrc ! "
#         "video/x-raw(memory:NVMM), "
#         "width=(int)%d, height=(int)%d, "
#         "format=(string)NV12, framerate=(fraction)%d/1 ! "
#         "nvvidconv flip-method=%d ! "
#         "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
#         "videoconvert ! "
#         "video/x-raw, format=(string)BGR ! appsink"
#         % (
#             capture_width,
#             capture_height,
#             framerate,
#             flip_method,
#             display_width,
#             display_height,
#         )
#     )


# def gen_frames():  # generate frame by frame from camera
#     cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
#     if cap.isOpened():
#         while True:
#             success, frame = cap.read()
#             if not success:
#                 break
#             else:
#                 ret, buffer = cv2.imencode(".jpg", frame)
#                 frame = buffer.tobytes()
#                 yield (
#                     b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
#                 )  # concat frame one by one and show result

cam = CSICamera()

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("public/home.html")


@main.route("/about")
def about():
    return render_template("public/about.html", title="About")


@main.route("/video_feed")
def video_feed():
    return Response(
        cam.live_stream(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )
