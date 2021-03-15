ARG BASE_IMAGE
FROM ${BASE_IMAGE}

# # Enable PWM mix on Jetson Nano 
ENV SHELL /bin/bash
CMD cd /opt/jduck/Docker/enable_pwm && chmod +x enable_pwm.sh && bash ./enable_pwm.sh