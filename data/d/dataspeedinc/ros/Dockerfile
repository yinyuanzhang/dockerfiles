FROM ros:melodic-ros-base-bionic

# AWS APT mirrors
RUN sed -i 's+http://security.ubuntu.com/+http://archive.ubuntu.com/+g' /etc/apt/sources.list \
 && sed -i 's+http://archive.ubuntu.com/+http://us-east-1.ec2.archive.ubuntu.com/+g' /etc/apt/sources.list \
 && apt update \
 && rm -rf /var/lib/apt/lists/*

# Dataspeed APT server
RUN echo "deb [ arch=amd64 ] http://packages.dataspeedinc.com/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-dataspeed-public.list \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 66F84AE1EB71A8AC108087DCAF677210FF6D3CDA \
 && apt update \
 && rm -rf /var/lib/apt/lists/*

# Dataspeed rosdep
RUN echo "yaml http://packages.dataspeedinc.com/ros/ros-public-melodic.yaml melodic" > /etc/ros/rosdep/sources.list.d/30-dataspeed-public-melodic.list \
 && rosdep update

# APT upgrade and autoremove
RUN apt update \
 && apt upgrade -y \
 && apt autoremove -y \
 && rm -rf /var/lib/apt/lists/*

# Install build-essential
RUN apt update \
 && apt install build-essential -y \
 && rm -rf /var/lib/apt/lists/*

# Install git and ssh
RUN apt update \
 && apt install -y git ssh-client \
 && rm -rf /var/lib/apt/lists/*

# Preload APT package index
RUN apt update
