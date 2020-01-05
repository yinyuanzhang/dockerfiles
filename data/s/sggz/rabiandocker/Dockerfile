# This is an auto generated Dockerfile for ros:desktop-full
# generated from docker_images/create_ros_image.Dockerfile.em
#FROM osrf/ros:kinetic-desktop-xenial
FROM ros:kinetic-robot

# install ros packages
#RUN apt-get install -y apt-transport-https 

RUN apt-get update && apt-get install -y \
    ros-kinetic-desktop-full \
    openssh-client python-catkin-tools ros-kinetic-controller-manager ros-kinetic-catkin ros-kinetic-joint-state-controller ros-kinetic-gps-common libcgal-dev libcgal-qt5-dev ros-kinetic-tf protobuf-compiler openssh-server curl tree rsync git \
    && rm -rf /var/lib/apt/lists/* && mkdir -p /opt/husqvarna 

#RUN apt-get update 

#RUN apt-get install -y openssh-client python-catkin-tools ros-kinetic-catkin ros-kinetic-joint-state-controller ros-kinetic-gps-common ros-kinetic-tf protobuf-compiler openssh-server curl tree rsync git

#RUN	mkdir -p /opt/husqvarna 

ADD rab-sdk.tar.gz /opt/husqvarna

RUN	mv /opt/husqvarna/host /opt/husqvarna/rab-sdk && echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc && /bin/bash -c "source ~/.bashrc"

#RUN pwd
#RUN	ls -al
#RUN	ls -al host
#RUN	mv host rab-sdk 
#RUN	ls -l rab-sdk
#RUN	mkdir -p /opt/husqvarna
#RUN	rsync -a -r rab-sdk/ /opt/husqvarna/rab-sdk


#RUN	mv host rab-sdk && mkdir -p /opt/husqvarna && rsync -a -r rab-sdk/ /opt/husqvarna/rab-sdk

#RUN echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc

#ENTRYPOINT ["source ~/.bashrc"]
#CMD ["bash"]

WORKDIR /opt/husqvarna/rab-sdk

RUN ./relocate-sdk.sh

