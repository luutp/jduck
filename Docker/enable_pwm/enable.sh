#!/bin/bash
# DEFINES
DOCKER_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
# ----------------------------------INCLUDE---------------------------------------
source ${DOCKER_FOLDER}/configure.sh
# ----------------------------------DEFINE----------------------------------------

sudo docker run -it -d \
    --restart always \
    --runtime nvidia \
    --network host \
    --privileged \
    --device /dev/mem \
    --name=jduck_pwm \
    $JDUCK_PWM_IMAGE