FROM ubuntu:16.04

MAINTAINER bssthu

# Install java8 and Deps

RUN apt-get update && \
    apt-get install -y --no-install-recommends software-properties-common && \
    dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y --force-yes --no-install-recommends expect git wget \
        libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 \
        lib32z1 python curl unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Android SDK
RUN cd /opt && \
    wget --output-document=tools.zip --quiet \
        https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip  && \
    unzip tools.zip -d android-sdk-linux && \
    rm -f tools.zip && \
    chown -R root.root android-sdk-linux

# Setup environment
ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools

# Install sdk elements
COPY tools /opt/tools
RUN chmod +x /opt/tools/android-*.sh
ENV PATH ${PATH}:/opt/tools
RUN ["/opt/tools/android-accept-licenses.sh", "android-update-sdk.sh \
platform-tools build-tools;26.0.0 build-tools;26.0.1 build-tools;26.0.2 build-tools;26.0.3 \
platforms;android-26 extras;android;m2repository \
extras;google;m2repository extras;google;google_play_services"]

RUN which adb && \
    which android && \
    which sdkmanager

# Install Gradle
WORKDIR /usr/lib
ENV GRADLE_VERSION 4.1
RUN cd /usr/lib && \
    wget https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip --quiet && \
    unzip -q gradle-${GRADLE_VERSION}-all.zip && \
    ln -s "/usr/lib/gradle-${GRADLE_VERSION}" /usr/bin/gradle && \
    rm gradle-${GRADLE_VERSION}-all.zip

ENV GRADLE_HOME /usr/bin/gradle
ENV PATH $PATH:$GRADLE_HOME/bin

# GO to workspace
RUN mkdir -p /opt/workspace
WORKDIR /opt/workspace

