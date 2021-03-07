#!/bin/bash
# DEFINES
DOCKER_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
# ----------------------------------INCLUDE---------------------------------------
source $DOCKER_FOLDER/configure.sh
# ----------------------------------START----------------------------------------
./jupyter/enable.sh
