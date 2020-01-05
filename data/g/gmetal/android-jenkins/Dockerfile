# Android development environment for ubuntu precise (14.04 LTS).
# version 0.0.1
# Start with ubuntu precise (LTS).
FROM jenkins:1.596
#FROM jenkins:latest
MAINTAINER gmetaxas <gmetaxas@gmail.com>
USER root
# Fake a fuse install (to prevent ia32-libs-multiarch package from producing errors)
RUN apt-get update && apt-get -y install libfuse2
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
RUN wget http://dl.google.com/android/android-sdk_r23.0.2-linux.tgz && tar -xvzf android-sdk_r23.0.2-linux.tgz && mv android-sdk-linux /usr/local/android-sdk && rm android-sdk_r23.0.2-linux.tgz

#Install required packages
RUN apt-get update && apt-get install -y sudo libssl1.0.0 libssl-dev tcl make lib32stdc++6 p7zip lib32z1

# Install android ndk
RUN wget http://dl.google.com/android/ndk/android-ndk-r10d-linux-x86_64.bin && mv android-ndk-r10d-linux-x86_64.bin android-ndk-r10d-linux-x86_64.bin.7z && p7zip -d android-ndk-r10d-linux-x86_64.bin.7z && mv android-ndk-r10d /usr/local/android-ndk 

# Install apache ant
RUN wget http://archive.apache.org/dist/ant/binaries/apache-ant-1.8.4-bin.tar.gz && tar -xvzf apache-ant-1.8.4-bin.tar.gz && mv apache-ant-1.8.4 /usr/local/apache-ant && rm apache-ant-1.8.4-bin.tar.gz

ENV ANDROID_HOME /usr/local/android-sdk
ENV PATH $PATH:$ANDROID_HOME/tools
ENV PATH $PATH:$ANDROID_HOME/platform-tools
ENV PATH $PATH:$ANDROID_HOME/build-tools/20.0.1
ENV NDK /usr/local/android-ndk


# Install latest android (21 / 5.0.0) tools and system image.
RUN VER=`android list sdk --no-ui | grep "Android SDK Platform-tools" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Android SDK Tools" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Android SDK Build-tools" | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "SDK Platform Android 4.4.2, API 19" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Android Support Repository" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Android Support Library" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Google Play services, revision" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Google Repository" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Google Play APK Expansion Library" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Google Play Billing Library" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "Google Play Licensing Library" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER
RUN VER=`android list sdk --no-ui | grep "SDK Platform Android 5.0" | head -n 1 | awk '{print $1}' | sed -e 's/-//g'` && echo "y" | android update sdk --no-ui --filter $VER

RUN mkdir /usr/local/projects

ENV JENKINS_HOME /var/jenkins_home
RUN chown -R jenkins:jenkins /var/jenkins_home
RUN chmod 0777 -R /tmp
RUN chown -R jenkins:jenkins /usr/local

USER jenkins

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
ENV ANDROID_NDK /usr/local/android-ndk
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64
ENV PATH $PATH:$NDK

