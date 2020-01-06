# ====================================================================== #
# Android SDK Docker Image
# ====================================================================== #

# Base image
# ---------------------------------------------------------------------- #
FROM ubuntu:16.04

# Author
# ---------------------------------------------------------------------- #
LABEL blazsolar "blaz@kamino.si"

# Set the locale
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

# support multiarch: i386 architecture
# install Java
# install essential tools
RUN dpkg --add-architecture i386 && \
    apt-get update -y && \
    apt-get install -y libncurses5:i386 libc6:i386 libstdc++6:i386 lib32gcc1 lib32ncurses5 lib32z1 zlib1g:i386 && \
    apt-get install -y --no-install-recommends openjdk-8-jdk && \
    apt-get install -y git zip wget
# && \
#    apt-get install -y qt5-default

# Create a non-root user
RUN groupadd -g 8888 jenkins && \
	useradd -u 8887 -g 8888 -m jenkins

USER jenkins
WORKDIR /home/jenkins

# download and install Android SDK
# https://developer.android.com/studio/#downloads
ARG ANDROID_SDK_VERSION=4333796
RUN mkdir -p ~/sdk && cd ~/sdk && \
    wget -q https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_VERSION}.zip && \
    unzip *tools*linux*.zip && \
    rm *tools*linux*.zip

# set the environment variables
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV ANDROID_HOME /home/jenkins/sdk
ENV PATH ${PATH}:${GRADLE_HOME}/bin:${KOTLIN_HOME}/bin:${ANDROID_HOME}/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/tools/bin
ENV _JAVA_OPTIONS -XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap
ENV GRADLE_USER_HOME /home/jenkins/.gradle
ENV HOME /home/jenkins

# Gradle memmory config ### Not needed since that folder is mapped from host
# RUN mkdir /home/jenkins/.gradle && \
#    echo "org.gradle.jvmargs=-Xmx4000M -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8" > /home/jenkins/.gradle/gradle.properties

# accept the license agreements of the SDK components
COPY --chown=jenkins:jenkins license_accepter.sh /home/jenkins/
RUN /home/jenkins/license_accepter.sh $ANDROID_HOME && \
	rm /home/jenkins/license_accepter.sh

# Cleanup
USER root
RUN apt-get remove -y zip wget
USER jenkins