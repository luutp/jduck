#!/bin/bash
# DEFINES
DOCKER_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
# ----------------------------------INCLUDE---------------------------------------
source $DOCKER_FOLDER/configure.sh
# ----------------------------------DEFINE----------------------------------------

cp /etc/apt/trusted.gpg.d/jetson-ota-public.asc ../..

sudo docker build \
    --build-arg BASE_IMAGE=$NVIDIA_L4T_IMAGE \
    -t $JDUCK_BASE_IMAGE \
    -f Dockerfile \
    ../.. # /home/user_name/jduck as build context