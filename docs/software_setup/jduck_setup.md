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