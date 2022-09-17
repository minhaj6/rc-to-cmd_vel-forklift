#!/bin/bash

source /home/ubuntu/mhrover_ws/devel/setup.bash
source /etc/ros/env.sh

export ROS_HOME=/home/ubuntu/.ros
roslaunch channel_publisher channel.launch --wait
PID=$!
wait "$PID"
