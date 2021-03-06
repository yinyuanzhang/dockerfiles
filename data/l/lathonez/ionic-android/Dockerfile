FROM     ubuntu:18.04
LABEL maintainer="shazleto@gmail.com"

# set workdir to android home
WORKDIR /opt/android-sdk-linux

ENV DEBIAN_FRONTEND=noninteractive \
    ANDROID_HOME=/opt/android-sdk-linux \
    NODE_VERSION=8.12.0 \
    IONIC_VERSION=4.1.2 \
    CORDOVA_VERSION=8.0.0 \
    GRADLE_VERSION=4.10.2

# Install basics
RUN apt-get update &&  \
    apt-get install -y git wget curl unzip build-essential ruby ruby-dev ruby-ffi gcc make && \
    curl --retry 3 -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" && \
    tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 && \
    rm "node-v$NODE_VERSION-linux-x64.tar.gz" && \
    npm install -g cordova@"$CORDOVA_VERSION" ionic@"$IONIC_VERSION" && \
    npm cache clear --force

#ANDROID
#JAVA

# install python-software-properties (so you can do add-apt-repository)
RUN apt-get update && apt-get install -y -q software-properties-common  && \
    add-apt-repository ppa:webupd8team/java -y && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get update && apt-get -y install oracle-java8-installer

#ANDROID STUFF
RUN echo ANDROID_HOME="${ANDROID_HOME}" >> /etc/environment && \
    dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --force-yes expect ant wget zipalign libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1 qemu-kvm kmod && \
    apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install SDK Tools
RUN wget https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip && \
    unzip sdk-tools-linux-4333796.zip && \
    rm -f sdk-tools-linux-4333796.zip

# Install SDK
RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager "platforms;android-26" && \
    yes | ${ANDROID_HOME}/tools/bin/sdkmanager "build-tools;26.0.3" && \
    yes | ${ANDROID_HOME}/tools/bin/sdkmanager --update

# Install Gradle
RUN wget "https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" && \
    unzip -d /opt/gradle gradle-${GRADLE_VERSION}-bin.zip && \
    rm -rf gradle-${GRADLE_VERSION}-bin.zip

# Setup environment
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:/opt/tools:/opt/gradle/gradle-4.10.2/bin

# Accept any dangling licenses
RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses