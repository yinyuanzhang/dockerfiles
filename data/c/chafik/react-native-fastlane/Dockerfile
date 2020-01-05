FROM starefossen/ruby-node:latest

MAINTAINER Chafik Hnini "chafik.hnini@gmail.com"

RUN gem install cocoapods:1.7.3 fastlane:2.128.1 --no-document

# JDK
ARG JAVA_VERSION=8
RUN apt-get update && \
    apt-get install -y openjdk-${JAVA_VERSION}-jdk
ENV JAVA_HOME /usr/lib/jvm/java-${JAVA_VERSION}-openjdk-amd64/

# Android SDK
ARG ANDROID_SDK_VERSION=4333796
RUN apt-get install -y unzip && \
    mkdir -p /opt/android-sdk && cd /opt/android-sdk && \
    wget -q https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_VERSION}.zip && \
    unzip *tools*linux*.zip && \
    rm *tools*linux*.zip
ENV ANDROID_HOME /opt/android-sdk
RUN mkdir /root/.android && \
    touch /root/.android/repositories.cfg && \
    yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses && \
    ${ANDROID_HOME}/tools/bin/sdkmanager --update
