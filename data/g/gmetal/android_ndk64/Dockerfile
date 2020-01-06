# Android development environment for ubuntu precise (14.04 LTS).
# version 0.0.1
# Start with ubuntu precise (LTS).
FROM ubuntu:14.04
MAINTAINER gmetaxas <gmetaxas@gmail.com>
# Never ask for confirmations
ENV DEBIAN_FRONTEND noninteractive
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-set-selections
# Update apt
RUN apt-get update
# First, install add-apt-repository and bzip2
RUN apt-get -y install python-software-properties bzip2
# Update apt
RUN apt-get update
#install add-apt-repository
RUN apt-get -y install software-properties-common
# Add oracle-jdk6 to repositories
RUN add-apt-repository ppa:webupd8team/java
# Update apt
RUN apt-get update
# Install oracle-jdk6
RUN apt-get -y install oracle-java6-installer
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
RUN wget http://dl.google.com/android/android-sdk_r23.0.2-linux.tgz
RUN tar -xvzf android-sdk_r23.0.2-linux.tgz
RUN mv android-sdk-linux /usr/local/android-sdk
# Install android ndk
RUN wget http://dl.google.com/android/ndk/android-ndk-r10c-linux-x86_64.bin
RUN sudo apt-get update && apt-get install  -y p7zip
RUN mv android-ndk-r10c-linux-x86_64.bin android-ndk-r10c-linux-x86_64.bin.7z && p7zip -d android-ndk-r10c-linux-x86_64.bin.7z
RUN mv android-ndk-r10c /usr/local/android-ndk
# Install apache ant
RUN wget http://archive.apache.org/dist/ant/binaries/apache-ant-1.8.4-bin.tar.gz
RUN tar -xvzf apache-ant-1.8.4-bin.tar.gz
RUN mv apache-ant-1.8.4 /usr/local/apache-ant

# Add android tools and platform tools to PATH
ENV ANDROID_HOME /usr/local/android-sdk
ENV PATH $PATH:$ANDROID_HOME/tools
ENV PATH $PATH:$ANDROID_HOME/platform-tools
ENV PATH $PATH:$ANDROID_HOME/build-tools/20.0.1
ENV NDK /usr/local/android-ndk

# Add ant to PATH
ENV ANT_HOME /usr/local/apache-ant
ENV PATH $PATH:$ANT_HOME/bin
# Export JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-6-oracle

#Install required packages
RUN sudo apt-get -y install lib32z1
RUN sudo apt-get update && apt-get install  -y make git gcc openssl
RUN sudo apt-get update && apt-get install  -y libssl1.0.0 libssl-dev
RUN sudo apt-get update && apt-get install  -y tcl
RUN sudo apt-get -y install make
RUN sudo apt-get -y install lib32stdc++6

# Remove compressed files.
RUN cd /; rm android-sdk_r23.0.2-linux.tgz && rm apache-ant-1.8.4-bin.tar.gz
# Install latest android (21 / 5.0.0) tools and system image.
RUN VER=`android list sdk --no-ui | grep "Android SDK Platform-tools" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Android SDK Tools" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Android SDK Build-tools" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "SDK Platform Android 4.4W, API 20" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "SDK Platform Android 5.0" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "SDK Platform Android 4.4.2, API 19" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Android Support Repository" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Android Support Library" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Google Play services, revision" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Google Repository" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Google Play APK Expansion Library" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Google Play Billing Library" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Google Play Licensing Library" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER

RUN mkdir /usr/local/projects

ENV PATH $PATH:$NDK
