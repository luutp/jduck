#!/bin/bash
# DEFINES
DOCKER_FOLDER=${PWD}
echo -e "\e[35m Docker Folder: ${DOCKER_FOLDER} \e[0m"
# ----------------------------------INCLUDE---------------------------------------
source $DOCKER_FOLDER/configure.sh
# ----------------------------------START----------------------------------------
cd jupyter && chmod +x enable.sh && bash ./enable.sh && cd ..
cd enable_pwm && chmod +x enable.sh && bash ./enable.sh && cd ..