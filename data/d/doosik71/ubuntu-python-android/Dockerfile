FROM ubuntu:18.04

MAINTAINER Doosik Kim <doosik71@gmail.com>

LABEL description="Ubuntu 18.04, Python 3, Jupyter, Kivy, Android NDK"

ENV TERM=xterm

RUN groupadd user && \
    useradd -g user -d /home/user -m user

# Install packages.
RUN apt-get update && \
    apt-get install -y \
        apt-utils && \
    apt-get install -y \
        aidl \
        autoconf \
        autogen \
        automake \
        build-essential \
        clang \
        cmake \
        freeglut3 \
        freeglut3-dev \
        git \
        libffi-dev \
        libgl1-mesa-glx \
        libncurses5-dev \
        libncursesw5-dev \
        libsdl2-dev \
        libsqlite3-dev \
        libtinfo5 \
        libtool \
        mesa-utils \
        openjdk-8-jdk \
        pkg-config \
        python3 \
        python3-pip \
        unzip \
        vim \
        wget \
        zip \
        zlib1g-dev && \
    apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Change user account.
USER user

ENV ANDROIDSDK=~/.buildozer/android/platform/android-sdk
ENV ANDROIDNDK=~/.buildozer/android/platform/android-ndk-r17c

# Install python packages for buildozer and kivy.
RUN pip3 install --user \
        buildozer \
        cython \
        kivy \
        Pillow \
        pip \
        pygame \
        PyQt5 \
        PyQtWebEngine \
        python-for-android \
        virtualenv

# Install python packages for opencv and etc.
# RUN pip3 install --user \
#         graphviz \
#         jupyter \
#         matplotlib \
#         nbconvert \
#         notebook \
#         numpy \
#         opencv-python \
#         opencv-contrib-python \
#         scikit-learn \
#         scipy

# Create src folder.
RUN mkdir /home/user/src && \
    cd /home/user/src && \
    yes | /home/user/.local/bin/buildozer init

COPY main.py /home/user/src/main.py

WORKDIR /home/user/src

CMD ["/bin/bash"]
