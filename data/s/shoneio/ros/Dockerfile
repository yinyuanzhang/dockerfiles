FROM ros:kinetic

## Install base dependencies
RUN apt-get update && apt-get install -y \
    wget \
    sudo

## allow passwordless sudo
RUN echo "ALL            ALL = (ALL) NOPASSWD: ALL" > /etc/sudoers.d/passwordless-sudo

## Adding catkin tools
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu `lsb_release -sc` main" > /etc/apt/sources.list.d/ros-latest.list'
RUN wget http://packages.ros.org/ros.key -O - | apt-key add -
RUN apt-get update && apt-get install -y python-catkin-tools

## Deault ros workspace for root
RUN echo "source /opt/ros/kinetic/setup.bash" >> /etc/profile

## Create ros User
ENV USER=ros
RUN useradd -ms /bin/bash ${USER}
USER ${USER}
ENV HOME=/home/${USER}

## Setup catkin workpace
ENV CATKIN_WS=/home/${USER}/workspace
RUN mkdir -p ${CATKIN_WS}/src
WORKDIR ${CATKIN_WS}/src
RUN /bin/bash -l -c "catkin_init_workspace"
WORKDIR ${CATKIN_WS}
RUN /bin/bash -l -c "catkin build"

## Provide ros environment by default on login bash (-l)
RUN echo "source ${CATKIN_WS}/devel/setup.bash" >> ${HOME}/.bash_profile

## Source newly created devel file and update deps
RUN /bin/bash -l -c "rosdep update"

## Setup entrypoint
COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

## Configs
ENV ROS_HOSTNAME=master
ENV ROS_MASTER_URI=http://localhost:11311
