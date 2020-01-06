# The MiRo simulator uses Gazebo 7, which requires a ROS Kinetic install and thus Ubuntu 16 (Xenial)
FROM gazebo:libgazebo7-xenial


## Install ROS

# Setup ROS keys and sources
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 421C365BD9FF1F717815A3895523BAEEB01FA116
RUN echo "deb http://packages.ros.org/ros/ubuntu `lsb_release -sc` main" > /etc/apt/sources.list.d/ros-latest.list

# Install ROS packages
RUN apt-get update && apt-get install -y \
	ros-kinetic-ros-base \
	ros-kinetic-common-msgs \
	ros-kinetic-compressed-image-transport \
	ros-kinetic-image-transport \
	ros-kinetic-image-view \
	# ros-kinetic-perception \
	ros-kinetic-tf2-ros \
&& rm -rf /var/lib/apt/lists/*

# Bootstrap rosdep
RUN rosdep init \
&& rosdep update


## Set environment variables

# Docker
ENV DISPLAY :0
ENV QT_X11_NO_MITSHM 1
ENV XAUTHORITY /root/.Xauthority

# ROS
ENV CATKIN_SHELL bash
ENV ROS_DISTRO kinetic
ENV ROS_ETC_DIR /opt/ros/$ROS_DISTRO/etc/ros
ENV ROS_IP 172.17.0.1
ENV ROS_MASTER_IP localhost
ENV ROS_MASTER_URI http://localhost:11311
ENV ROS_PACKAGE_PATH=/root/mdk/catkin_ws/install/share:/opt/ros/$ROS_DISTRO/share
ENV ROS_ROOT /opt/ros/$ROS_DISTRO/share/ros

# Gazebo
ENV GAZEBO_MODEL_PATH /root/mdk/sim/models
ENV GAZEBO_PLUGIN_PATH /root/mdk/bin/deb64
ENV GAZEBO_RESOURCE_PATH /root/mdk/sim

# MiRo
ENV MIRO_DIR_CONFIG /root/.miro2/config

# System
ENV CMAKE_PREFIX_PATH /root/mdk/catkin_ws/install:/opt/ros/$ROS_DISTRO
ENV LD_LIBRARY_PATH /root/mdk/catkin_ws/install/lib:/opt/ros/$ROS_DISTRO/lib:/opt/ros/$ROS_DISTRO/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu/gazebo-7/plugins
ENV PATH=/opt/ros/$ROS_DISTRO/bin:/root/bin:/root/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
ENV PKG_CONFIG_PATH /root/mdk/catkin_ws/install/lib/pkgconfig:/opt/ros/$ROS_DISTRO/lib/pkgconfig:/opt/ros/$ROS_DISTRO/lib/x86_64-linux-gnu/pkgconfig
ENV PYTHONPATH /root/mdk/share/python:/root/mdk/catkin_ws/install/lib/python2.7/dist-packages:/opt/ros/$ROS_DISTRO/lib/python2.7/dist-packages


## These variables are set by the MDK but are not needed unless running client_demo from within Docker
#ENV MIRO_DIR_STATE /tmp/miro2/state
#ENV MIRO_DIR_DUMP /tmp/miro2/dump
#ENV MIRO_BRIDGE_FLAGS l
#ENV MIRO_DIR_BIN /root/mdk/bin/deb64
#ENV MIRO_DIR_LOG /tmp/miro2/log
#ENV MIRO_DIR_ONBOARD /root/mdk/bin/onboard
#ENV MIRO_DIR_MDK /root/mdk
#ENV MIRO_DIR_SHARE /root/mdk/share
#ENV MIRO_DIR_TMP /tmp/miro2
#ENV MIRO_DIR_TRASH /root/.miro2/trash
#ENV MIRO_DIR_USER /root/.miro2
#ENV MIRO_EDITION 2
#ENV MIRO_MDK_RELEASE R190407
#ENV MIRO_MULTITOOL /root/mdk/bin/onboard/multitool.sh
#ENV MIRO_ROBOT_NAME miro
#ENV MIRO_ROS_RELEASE $ROS_DISTRO
#ENV MIRO_SYSTEM deb64
#ENV MIRO_TOKEN miro2
#ENV MIRO_USER_SETUP /root/.miro2/config/user_setup.bash


# Add MiRo MDK and config files
# MDK available from http://labs.consequentialrobotics.com/miro-e/software/
# .miro2 directory generated from a successful MDK install
COPY mdk /root/mdk/
COPY miro2 /root/.miro2

# Execute command
COPY run.sh /usr/local/bin/run.sh
RUN chmod +x /usr/local/bin/run.sh
CMD /usr/local/bin/run.sh

# Note that Gazebo will sometimes fail with a BadDrawable error, just keep retrying until it works!
# This is a known Gazebo bug:
# https://github.com/vvv-school/assignment_computed-torque/issues/3#issuecomment-364370433
