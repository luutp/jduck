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
import matplotlib.pyplot as plt

# Custom Packages
from utils.logging_config import logger as logging


# =====================================DEFINES=================================

script_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.dirname(script_dir)

# =====================================START=================================


def bgr8_to_jpeg(value, quality=75):
    return bytes(cv2.imencode(".jpg", value)[1])


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
        self._values = None
        try:
            self.cam = cv2.VideoCapture(self._gst_str(), cv2.CAP_GSTREAMER)

            re, frame = self.cam.read()

            if not re:
                raise RuntimeError("Could not read image from camera.")
            else:
                logging.info("CSI Camera Initiated Successfully")
        except Exception as e:
            logging.error(e)
            self.stop()
            raise RuntimeError("Could not initialize camera.  Please see error trace.")
        self.values = frame
        self.start()

    @property
    def flip_method(self):
        return self._flip_method

    @flip_method.setter
    def flip_method(self, inputVal):
        self._flip_method = inputVal

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, inputVal):
        self._values = inputVal

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

    def start(self):
        if not self.cam.isOpened():
            self.cam.open(self._gst_str(), cv2.CAP_GSTREAMER)
        if not hasattr(self, "thread") or not self.thread.isAlive():
            self.thread = threading.Thread(target=self.web_stream)
            self.thread.start()

    def stop(self):
        if hasattr(self, "cam"):
            self.cam.release()
        if hasattr(self, "thread"):
            self.thread.join()

    def restart(self):
        self.stop()
        self.start()

    def get_frame(self):
        re, frame = self.cam.read()
        if re:
            self.values = frame
            return frame
        else:
            raise RuntimeError("Could not read image from camera")

    def show_frame(self):
        frame = self.get_frame()
        img_data = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.imshow(img_data)
        ax.set_aspect("equal")
        ax.axis("off")

    def web_stream(self):
        while True:
            success, frame = self.cam.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode(".jpg", frame)
                frame = buffer.tobytes()
                yield (
                    b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
                )

    @staticmethod
    def instance(*args, **kwargs):
        return CSICamera(*args, **kwargs)


# # =====================================MAIN==========================================

# # # def main():
# cam = CSICamera()
# print(cam)
# #%%
# cam.stop()
# #%%
# cam.show_frame()
# #%%
# cam.start()
# #%%
# cam.web_stream()
#%%
# cam.live_stream()
# main()
#%%
# =====================================DEBUG=========================================

# if __name__ == "__main__":
#     main()
# =========================================================================
