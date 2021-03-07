#!/bin/bash
# DEFINES
DOCKER_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
# ----------------------------------INCLUDE---------------------------------------
source ${DOCKER_FOLDER}/configure.sh
# ----------------------------------DEFINE----------------------------------------
WORKSPACE=$1
JDUCK_CAMERA=${2:-opencv_gst_camera}

sudo docker run -it -d \
    --restart always \
    --runtime nvidia \
    --network host \
    --privileged \
    --device /dev/video* \
    --device /dev/mem \
    --volume /dev/bus/usb:/dev/bus/usb \
    --volume /tmp/argus_socket:/tmp/argus_socket \
    -p 8888:8888 \
    -v $WORKSPACE:/workspace \
    --workdir /workspace \
    --name=jduck_jupyter \
    --memory-swap=$JDUCK_JUPYTER_MEMORY_SWAP \
    --env JDUCK_DEFAULT_CAMERA=$JDUCK_CAMERA \
    $JDUCK_JUPYTER_IMAGE
