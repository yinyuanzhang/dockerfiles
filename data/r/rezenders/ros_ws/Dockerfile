FROM rezenders/armv7hf-ubuntu-openjdk-ros:8-jdk-bionic 

RUN apt-get update && apt-get install -y \
    vim \
    && rm -rf /var/lib/apt/lists/

# Setup catkin workspace
RUN ["/bin/bash","-c", "source /opt/ros/melodic/setup.bash && \
                  mkdir -p /catkin_ws/src && \
                  cd /catkin_ws/src && \
                  catkin_init_workspace && \
                  cd /catkin_ws/ && \
                  catkin_make "]

WORKDIR /catkin_ws/src/

#Copy package files to catkin workspace
RUN catkin_create_pkg keyboard_driver
COPY teleop_ws/src/keyboard_driver /catkin_ws/src/keyboard_driver

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]
