FROM ubuntu:18.04

ENV ROS_DISTRO=bouncy
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    # Install base packages \
    && apt-get install -y --no-install-recommends curl gnupg ca-certificates wget python3 tzdata bash \
    # Configure TimeZone for tzdata package \
    && ln -fs /usr/share/zoneinfo/UTC /etc/localtime \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    # Add Ros2 Repository \
    && curl http://repo.ros2.org/repos.key | apt-key add - \
    && echo "deb [arch=amd64,arm64] http://repo.ros2.org/ubuntu/main bionic main" > /etc/apt/sources.list.d/ros2-latest.list \
    && apt-get update \
    # Install packages \
    && apt-get install -y --no-install-recommends ros-${ROS_DISTRO}-ros-base \
                                                  build-essential \
                                                  cmake \
                                                  git \
                                                  python3-colcon-common-extensions \
                                                  python3-pip \
                                                  python-rosdep \
                                                  python3-vcstool \
                                                  libasio-dev \
                                                  libtinyxml2-dev \
                                                  libpython3-dev \
    && rm -rf /var/lib/apt/lists/* \
    # Install some pip packages needed for testing \
    && python3 -m pip install --quiet --no-cache-dir -U argcomplete \
                                                        flake8 \
                                                        flake8-blind-except \
                                                        flake8-builtins \
                                                        flake8-class-newline \
                                                        flake8-comprehensions \
                                                        flake8-deprecated \
                                                        flake8-docstrings \
                                                        flake8-import-order \
                                                        flake8-quotes \
                                                        pytest-repeat \
                                                        pytest-rerunfailures

ENTRYPOINT ["/usr/bin/rosdep"]
