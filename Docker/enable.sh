#!/bin/bash
# ----------------------------------DEFINE----------------------------------------
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
PROJECT_NAME="${PWD##*/}"

export JDUCK_VERSION=0.1.1

L4T_VERSION_STRING=$(head -n 1 /etc/nv_tegra_release)
L4T_RELEASE=$(echo $L4T_VERSION_STRING | cut -f 2 -d ' ' | grep -Po '(?<=R)[^;]+')
L4T_REVISION=$(echo $L4T_VERSION_STRING | cut -f 2 -d ',' | grep -Po '(?<=REVISION: )[^;]+')

export L4T_VERSION="$L4T_RELEASE.$L4T_REVISION"

if [[ "$L4T_VERSION" == "32.4.3" ]]
then
    # docker hub 
    export JDUCK_ DOCKER_REMOTE=jduck
elif [[ "$L4T_VERSION" == "32.4.4" ]]
then
    export JDUCK_DOCKER_REMOTE=jduck
fi

./set_nvidia_runtime.sh
# sudo systemctl enable docker

# check system memory
SYSTEM_RAM_KILOBYTES=$(awk '/^MemTotal:/{print $2}' /proc/meminfo)

if [ $SYSTEM_RAM_KILOBYTES -gt 3000000 ]
then
    export JDUCK_JUPYTER_MEMORY=500m
    export JDUCK_JUPYTER_MEMORY_SWAP=3G
fi

JUPYTER_WORKSPACE=${1:-$HOME}  # default to $HOME
JDUCK_CAMERA=${2:-opencv_gst_camera}  # default to opencv

echo ${SYSTEM_RAM_KILOBYTES}

# if [ "$jduck_CAMERA" = "zmq_camera" ]
# then
# 	./camera/enable.sh
# fi

# ./display/enable.sh
# ./jupyter/enable.sh $JUPYTER_WORKSPACE $jduck_CAMERA