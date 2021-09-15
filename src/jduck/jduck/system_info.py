#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
system_info.py
Description:

Author: PhatLuu
Contact: tpluu2207@gmail.com
Created on: 2021/09/14
"""

#%%
# ================================IMPORT PACKAGES====================================

# Standard Packages
import argparse
import errno
import os
import shutil
import subprocess

# Web pages and URL Related
import requests

# Utilities
import time
from datetime import datetime
from tqdm import tqdm


# =====================================DEFINES=================================
script_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.dirname(script_dir)

# =====================================START================================= # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
def get_cpu_usage():
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell=True)
    return CPU.decode("utf-8")


def get_mem_usage():
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell=True)
    return MemUsage.decode("utf-8")


def get_disk_usage():
    cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%dGB %s", $3,$2,$5}\''
    Disk = subprocess.check_output(cmd, shell=True)
    return Disk.decode("utf-8")


def get_network_interface_state(interface):
    if not os.path.exists("/sys/class/net/%s/operstate" % interface):
        # print("%s file does NOT exist" % interface)
        return None
    try:
        status = subprocess.check_output(
            "cat /sys/class/net/%s/operstate" % interface, shell=True
        ).decode("ascii")[:-1]
    except Exception as err:
        print("Exception: {0}".format(err))
        return None
    else:
        return status


def get_ip_address(interface):
    state = get_network_interface_state(interface)
    if state == "down" or state == None:
        return None
    cmd = (
        "ifconfig %s | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'"
        % interface
    )
    return subprocess.check_output(cmd, shell=True).decode("ascii")[:-1]


#%%

# print(get_ip_address("eth0"))
# print(get_disk_usage())
# print(get_ip_address('wlan0'))
#%%
