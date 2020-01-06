# This is an auto generated Dockerfile for ros:desktop-full
# generated from docker_images/create_ros_image.Dockerfile.em
#FROM osrf/ros:kinetic-desktop-xenial

ARG from=osrf/ros:kinetic-desktop-xenial

#FROM ianblenke/xfce:latest
#FROM x11docker/xfce
FROM nvidia/opengl:1.0-glvnd-runtime-ubuntu16.04 as nvidia
FROM ${from}


COPY --from=nvidia /usr/local /usr/local
COPY --from=nvidia /etc/ld.so.conf.d/glvnd.conf /etc/ld.so.conf.d/glvnd.conf

ENV NVIDIA_VISIBLE_DEVICES=all NVIDIA_DRIVER_CAPABILITIES=all

# add chinese source
ADD sources.list /etc/apt/

# install ros packages
RUN apt-get update && apt-get install -y \
    ros-kinetic-desktop-full=1.3.2-0* \
    && rm -rf /var/lib/apt/lists/*

########################### install windows manager ########################################
#krusader
RUN apt-get update && apt install -y --no-install-recommends vim and terminator and konsole and krusader && rm -rf /var/lib/apt/lists/*
#RUN apt-get update && apt install -y --no-install-recommends dolphin and nautilus and thunar and pcmanfm && rm -rf /var/lib/apt/lists/*


#ENV DEBIAN_FRONTEND teletype


########################## install desktop environment########################################

# install xfce Desktop
#RUN apt-get update && apt-get install -y --no-install-recommends xfce4 && rm -rf /var/lib/apt/lists/*

# install gnome Desktop
#RUN apt-get update && apt-get install -y --no-install-recommends gnome && rm -rf /var/lib/apt/lists/*

# install kde Desktop
#RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y kubuntu-desktop && apt-get clean && rm -rf /var/lib/apt/lists/*

# install LXDE Desktop
RUN apt-get update && apt install -y --no-install-recommends lxde && rm -rf /var/lib/apt/lists/*

########################### install vnc ########################################
# Install vnc, xvfb in order to create a 'fake' display and firefox
RUN apt-get update && apt-get install -y x11vnc xvfb firefox
RUN mkdir ~/.vnc
# Setup a password
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd
# Autostart firefox (might not be the best way, but it does the trick)
RUN bash -c 'echo "firefox" >> /.bashrc'

EXPOSE 5900

#CMD    ["x11vnc", "-forever", "-usepw", "-create"]

#x11vnc -forever -usepw -create

####################################################################################


ENV DISPLAY=172.17.0.1:0

#VOLUME /home/wang /home/wang

# allow chinese input
ENV LANG=C.UTF-8










