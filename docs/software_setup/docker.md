# Docker

``` bash
📂Docker
┣ 📂base
┃ ┣ 🐋Dockerfile
┃ ┗ 📜build.sh
┣ 📂enable_pwm
┃ ┣ 🐋Dockerfile
┃ ┣ 📜build.sh
┃ ┣ 📜enable.sh
┃ ┗ 📜enable_pwm.sh
┣ 📂jupyter
┃ ┣ 🐋Dockerfile
┃ ┣ 📜build.sh
┃ ┣ 📜disable.sh
┃ ┗ 📜enable.sh
┣ 📜build.sh
┣ 📜configure.sh
┣ 📜disable.sh
┣ 📜enable.sh
┗ 📜set_nvidia_runtime.sh
```

<div style="text-align:center"> 
	<img src="../images/646984561.png" width=50% alt="646984561"> 
	<figcaption>Jetson Nano Developer Kit 40-Pin Header (J6)</figcaption> 
</div>

**Pins 32 and 33** of the Jetson Nano Developer Kit could be configured to be used as PWM outputs. 
However, they are specfied by default as **GPIO_PV00 and GPIO_PE06**, respectively. To enable PWM outputs for these pins, we need to run the following bash command for **Pinmux** re-configuration

???+ info "Enable PWM"
	``` bash
    #!/bin/bash
    # Enable PWM on jetson nano
    # Enable Pin 32 / PWM0
    busybox devmem 0x700031fc 32 0x45
    busybox devmem 0x6000d504 32 0x2
    # Enable Pin 33 / PWM2
    busybox devmem 0x70003248 32 0x46
    busybox devmem 0x6000d100 32 0x00
  	```
