# Android development environment for Ubuntu 14.04 LTS.
# version 0.0.1

# Start with Ubuntu 14.04 LTS.
FROM ubuntu:14.04

MAINTAINER Ryan Harter <ryanjharter@gmail.com>

# Never ask for confirmations
ENV DEBIAN_FRONTEND noninteractive
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-set-selections

# First, install add-apt-repository and bzip2
RUN apt-get -y install software-properties-common python-software-properties bzip2 unzip openssh-client git lib32stdc++6 lib32z1

# Add oracle-jdk6 to repositories
RUN add-apt-repository ppa:webupd8team/java

# Make sure the package repository is up to date
#RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list

# Update apt
RUN apt-get update

# Install oracle-jdk7
RUN apt-get -y install oracle-java7-installer

# Fake a fuse install (to prevent ia32-libs-multiarch package from producing errors)
RUN apt-get install libfuse2
RUN cd /tmp ; apt-get download fuse
RUN cd /tmp ; dpkg-deb -x fuse_* .
RUN cd /tmp ; dpkg-deb -e fuse_*
RUN cd /tmp ; rm fuse_*.deb
RUN cd /tmp ; echo -en '#!/bin/bash\nexit 0\n' > DEBIAN/postinst
RUN cd /tmp ; dpkg-deb -b . /fuse.deb
RUN cd /tmp ; dpkg -i /fuse.deb

# Install support libraries for 32-bit
#RUN apt-get -y install ia32-libs-multiarch

# Install android sdk
RUN wget http://dl.google.com/android/android-sdk_r22.6.2-linux.tgz
RUN tar -xvzf android-sdk_r22.6.2-linux.tgz
RUN mv android-sdk-linux /usr/local/android-sdk
RUN rm android-sdk_r22.6.2-linux.tgz

# Install Android tools
RUN echo y | /usr/local/android-sdk/tools/android update sdk --filter tools,platform-tools,build-tools-19.1.0,android-19,extra-google-google_play_services,extra-android-support,extra-android-m2repository,extra-google-analytics_sdk_v2 --no-ui --force -a

# Install android ndk
# RUN wget http://dl.google.com/android/ndk/android-ndk-r9d-linux-x86_64.tar.bz2
# RUN tar -xvjf android-ndk-r9d-linux-x86_64.tar.bz2
# RUN mv android-ndk-r9d /usr/local/android-ndk

# Install apache ant
# RUN cd /usr/local/ && curl -L -O http://ftp.meisei-u.ac.jp/mirror/apache/dist//ant/binaries/apache-ant-1.9.2-bin.tar.gz && tar xf apache-ant-1.9.2-bin.tar.gz

# Install Gradle
RUN wget https://services.gradle.org/distributions/gradle-1.12-all.zip
RUN unzip -o gradle-1.12-all.zip
RUN mv gradle-1.12 /usr/local/gradle
RUN rm gradle-1.12-all.zip

# Environment variables
ENV ANDROID_HOME /usr/local/android-sdk
ENV GRADLE_HOME /usr/local/gradle
ENV PATH $PATH:$ANDROID_HOME/tools
ENV PATH $PATH:$ANDROID_HOME/platform-tools
ENV PATH $PATH:$GRADLE_HOME/bin

# Export JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle
