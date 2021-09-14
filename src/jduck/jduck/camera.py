#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
camera.py
Description:

Author: PhatLuu
Contact: tpluu2207@gmail.com
Created on: 2021/09/14
"""

#%%
# ================================IMPORT PACKAGES====================================

# Standard Packages
import inspect
import os
import threading
from abc import ABC
from abc import abstractclassmethod

# Visualization Packages
import cv2

# Custom Packages
from utils.logging_config import logger as logging


# =====================================DEFINES=================================

script_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.dirname(script_dir)

# =====================================START=================================


class BaseCamera(ABC):
    @property
    def fps(self):
        return self._fps

    @fps.setter
    def fps(self, inputVal):
        self._fps = inputVal

    @property
    def frame_width(self):
        return self._frame_width

    @frame_width.setter
    def frame_width(self, inputVal):
        self._frame_width = inputVal

    @property
    def frame_height(self):
        return self._frame_height

    @frame_height.setter
    def frame_height(self, inputVal):
        self._frame_height = inputVal

    @abstractclassmethod
    def get_frame(self):
        pass

    # @abstractclassmethod
    # def stream(self):
    #     pass

    def __str__(self):
        str_output = ""
        for mem in self.get_obj_attrs(self):
            str_output += f"{mem[0]:25s}: {mem[1]}\n"
        return str_output

    @staticmethod
    def get_obj_attrs(obj):
        members = inspect.getmembers(obj)
        attr_members = []
        for mem in members:
            if not inspect.isfunction(mem[1]) and not inspect.ismethod(mem[1]):
                if not mem[0].startswith("__"):
                    attr_members.append(mem)
        return attr_members


class CSICamera(BaseCamera):
    # Initialize Class
    def __init__(self, frame_width=480, frame_height=360, fps=30):
        self._frame_width = frame_width
        self._frame_height = frame_height
        self._fps = fps
        self._flip_method = 0
        try:
            self.cam = cv2.VideoCapture(self._gst_str(), cv2.CAP_GSTREAMER)

            re, image = self.cam.read()

            if not re:
                raise RuntimeError("Could not read image from camera.")
            else:
                logging.info("CSI Camera Initiated Successfully")
        except Exception as e:
            logging.error(e)
            raise RuntimeError("Could not initialize camera.  Please see error trace.")

    @property
    def flip_method(self):
        return self._flip_method

    @flip_method.setter
    def flip_method(self, inputVal):
        self._flip_method = inputVal

    def _gst_str(self):
        capture_width = self.frame_width
        capture_height = self.frame_height
        display_width = self.frame_width
        display_height = self.frame_height
        framerate = self.fps
        flip_method = self.flip_method
        return (
            "nvarguscamerasrc ! "
            "video/x-raw(memory:NVMM), "
            "width=(int)%d, height=(int)%d, "
            "format=(string)NV12, framerate=(fraction)%d/1 ! "
            "nvvidconv flip-method=%d ! "
            "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
            "videoconvert ! "
            "video/x-raw, format=(string)BGR ! appsink"
            % (
                capture_width,
                capture_height,
                framerate,
                flip_method,
                display_width,
                display_height,
            )
        )

    def get_frame(self):
        re, image = self.cam.read()
        if re:
            return image
        else:
            raise RuntimeError("Could not read image from camera")

    def live_stream(self):
        if self.cam.isOpened():
            while True:
                success, frame = self.cam.read()
                if not success:
                    break
                else:
                    ret, buffer = cv2.imencode(".jpg", frame)
                    frame = buffer.tobytes()
                    yield (
                        b"--frame\r\n"
                        b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
                    )


# =====================================MAIN==========================================


def main():
    cam = CSICamera()
    cam.live_stream()


# main()
#%%
# =====================================DEBUG=========================================

if __name__ == "__main__":
    main()
# =========================================================================


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
#                 )
