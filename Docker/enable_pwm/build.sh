#!/bin/bash
# DEFINES
DOCKER_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
# ----------------------------------INCLUDE---------------------------------------
source ${DOCKER_FOLDER}/configure.sh
# ----------------------------------DEFINE----------------------------------------
sudo docker build \
    --build-arg BASE_IMAGE=$JDUCK_BASE_IMAGE \
    -t $JDUCK_PWM_IMAGE \
    -f Dockerfile .