#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
DCMotor.py
Description:

Author: luutp
Contact: luubot2207@gmail.com
Created on: 2021/02/27
'''

# %%
# ================================IMPORT PACKAGES====================================

import Jetson.GPIO as GPIO
import traitlets
from traitlets.config.configurable import Configurable
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# %%

class DCMotor(Configurable):
    value = traitlets.Float()

    def __init__(self, pwm_pin, ctrl_pin1, ctrl_pin2, **kwargs):
        self.pwm_pin = pwm_pin
        self.ctrl_pin1 = ctrl_pin1
        self.ctrl_pin2 = ctrl_pin2
        # Motor calibration
        self.alpha = kwargs.get('alpha', 1.0)
        self.beta = kwargs.get('beta', 0.0)
        # GPIO setup
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, 50)  # (channel, frequency)
        self.pwm.start(0)
        self.speed = 0
        GPIO.setup(self.ctrl_pin1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.ctrl_pin2, GPIO.OUT, initial=GPIO.LOW)

    @traitlets.observe('value')
    def _observe_value(self, change):
        self._write_value(change['new'])

    def _write_value(self, value):
        """Sets motor value between [-1, 1]"""
        mapped_value = int(100.0 * (self.alpha * value + self.beta))
        speed = min(max(abs(mapped_value), 0), 100)
        self.set_speed(speed)
        if mapped_value > 0:
            self.rotate_forward()
        else:
            self.rotate_backward()

    def set_speed(self, normalized_speed):
        # normalized_speed in percentange from 0 - 100
        self.pwm.ChangeDutyCycle(normalized_speed)
        self.speed = normalized_speed

    def rotate_forward(self):
        GPIO.output(self.ctrl_pin1, GPIO.LOW)
        GPIO.output(self.ctrl_pin2, GPIO.HIGH)

    def rotate_backward(self):
        GPIO.output(self.ctrl_pin1, GPIO.HIGH)
        GPIO.output(self.ctrl_pin2, GPIO.LOW)

    def stop(self):
        GPIO.output(self.ctrl_pin1, GPIO.LOW)
        GPIO.output(self.ctrl_pin2, GPIO.LOW)
