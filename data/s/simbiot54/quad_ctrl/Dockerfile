# This is an auto generated Dockerfile for ros:kinetic-perception
# generated from templates/docker_images/create_ros_image.Dockerfile.em
# generated on 2017-01-27 02:34:03 +0000
FROM ros:kinetic-ros-base

# install ros packages
RUN apt-get update && apt-get install -y \
    ros-kinetic-perception=1.3.0-0* \
    && rm -rf /var/lib/apt/lists/*

ADD app /app

RUN apt-get update && apt-get install -y \
    python-catkin-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/grone_ws
RUN /bin/bash -c 'source /opt/ros/kinetic/setup.sh \
    && catkin build'
    
    



