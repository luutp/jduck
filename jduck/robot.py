#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
jduck.py
Description:

Author: luutp
Contact: luubot2207@gmail.com
Created on: 2021/02/27
'''

# %%
# ================================IMPORT PACKAGES====================================
from traitlets.config.configurable import SingletonConfigurable

from DCMotor import DCMotor

# ================================================================================

class JDuck(SingletonConfigurable):
    def __init__(self, *args, **kwargs):
        self.left_motor = DCMotor(32, 36, 38, alpha=1.0)
        self.right_motor = DCMotor(33, 35, 37, alpha=1.0)
        self.left_motor.set_speed(50)
        self.right_motor.set_speed(50)

    def set_speeds(self, left_speed, right_speed):
        self.left_motor.set_speed(left_speed)
        self.right_motor.set_speed(right_speed)

    def move_forward(self):
        self.left_motor.rotate_forward()
        self.right_motor.rotate_forward()

    def move_backward(self):
        self.left_motor.rotate_backward()
        self.right_motor.rotate_backward()

    def turn_left(self):
        self.left_motor.rotate_backward()
        self.right_motor.rotate_forward()

    def turn_right(self):
        self.left_motor.rotate_forward()
        self.right_motor.rotate_backward()

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
