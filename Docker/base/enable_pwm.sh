#!/bin/bash
# Enable PWM on jetson nano
# Enable Pin 32 / PWM0
busybox devmem 0x700031fc 32 0x45
busybox devmem 0x6000d504 32 0x2
# Enable Pin 33 / PWM2
busybox devmem 0x70003248 32 0x46
busybox devmem 0x6000d100 32 0x00