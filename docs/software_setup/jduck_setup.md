# Software setup for jDuck using Docker Container

## Step1: Clone jduck repos from our github

``` sh
git clone http://github.com/luutp/jduck.git
```
## Step2: Build and enable Docker containers

``` sh
cd jduck/Docker
```

``` bash linenums="0"
📦Docker
 ┣ 📂base
 ┣ 📂enable_pwm
 ┣ 📂jupyter
 ┣ 📜build.sh
 ┣ 📜configure.sh
 ┣ 📜disable.sh
 ┣ 📜enable.sh
 ┗ 📜set_nvidia_runtime.sh
```

```sh
bash ./build.sh
```

``` bash
bash ./enable.sh
```

??? info "Docker Tips"
    Once you execute the enable.sh script, the containers are set to restart automatically. This means you can shut down your jDuck, and when you reboot the containers will run and you don't need to repeat this process.

    To prevent the containers from starting automatically, just call the disable.sh script.
    ``` bash
        cd ~/jduck/Docker
        bash ./disable.sh
    ```
