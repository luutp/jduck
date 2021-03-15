#!/bin/bash

# DEFINES
JDUCK_VERSION=0.1.0

L4T_VERSION_STRING=$(head -n 1 /etc/nv_tegra_release)
L4T_RELEASE=$(echo $L4T_VERSION_STRING | cut -f 2 -d ' ' | grep -Po '(?<=R)[^;]+')
L4T_REVISION=$(echo $L4T_VERSION_STRING | cut -f 2 -d ',' | grep -Po '(?<=REVISION: )[^;]+')
L4T_VERSION="$L4T_RELEASE.$L4T_REVISION"
if [[ "$L4T_VERSION" == "32.4.4" ]]
then
	NVIDIA_L4T_IMAGE=nvcr.io/nvidia/l4t-pytorch:r32.4.4-pth1.6-py3
else
	echo "NVIDIA_L4T_IMAGE not found for ${L4T_VERSION}. NOTE: The JDUCK containers currently target a Jetson Nano SD card image flashed with JetPack 4.4"
fi

JDUCK_DOCKER_REMOTE=jduck

# check system memory
SYSTEM_RAM_KILOBYTES=$(awk '/^MemTotal:/{print $2}' /proc/meminfo)

JDUCK_JUPYTER_MEMORY=500m
JDUCK_JUPYTER_MEMORY_SWAP=-1

JDUCK_BASE_IMAGE=$JDUCK_DOCKER_REMOTE/jduck:base-$JDUCK_VERSION-$L4T_VERSION
JDUCK_JUPYTER_IMAGE=$JDUCK_DOCKER_REMOTE/jduck:jupyter-$JDUCK_VERSION-$L4T_VERSION
JDUCK_PWM_IMAGE=$JDUCK_DOCKER_REMOTE/jduck:pwm-$JDUCK_VERSION-$L4T_VERSION

# -------------------------------------ECHO---------------------------------------
# echo "RAM: ${SYSTEM_RAM_KILOBYTES}"
# echo "L4T_VERSION: ${L4T_VERSION}"
# echo "JDUCK_VERSION: ${JDUCK_VERSION}"
# echo "JDUCK_DOCKER_REMOTE: ${JDUCK_DOCKER_REMOTE}"
