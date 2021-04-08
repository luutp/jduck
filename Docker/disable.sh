#!/bin/bash
# Stop and remove all docker images
list_containters(){
    echo "Current Containers:"
    echo $(sudo docker ps -a)
}
stop_all_containers(){
    echo "Stopping all containers..."
    sudo docker stop $(sudo docker ps -a -q)
    sudo docker rm $(sudo docker ps -a -q)
}
list_containters
stop_all_containers
list_containters