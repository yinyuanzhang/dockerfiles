FROM ubuntu:14.04

MAINTAINER devnull "devnull@myrealtrip.com"

ENV ANDROID_HOME /usr/local/android-sdk-linux

RUN apt-get update -q

# Install packages
RUN apt-get install -y \
  python-software-properties \
  software-properties-common \
  wget \
  unzip \
  --no-install-recommends

# Install git
RUN add-apt-repository ppa:git-core/ppa
RUN apt-get update -q
RUN apt-get -y install git
RUN git --version

# Install Java 8
RUN apt-add-repository ppa:openjdk-r/ppa
RUN apt-get update -q
RUN apt-get -y install openjdk-8-jdk
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure
RUN java -version

# Install Android linux sdk
RUN cd /usr/local \
 && wget -q https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip -O android-sdk-tools.zip \
 && unzip -q android-sdk-tools.zip -d ${ANDROID_HOME}\
 && rm android-sdk-tools.zip
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools

RUN mkdir ~/.android && touch ~/.android/repositories.cfg

# android licenses
RUN sdkmanager --update && yes | sdkmanager --licenses

# android platform-tools
RUN sdkmanager "platform-tools"

# android platform
RUN sdkmanager "platforms;android-26"

# android build-tools
RUN sdkmanager "build-tools;26.0.2"

# android extras
RUN sdkmanager "extras;android;m2repository"
RUN sdkmanager "extras;google;m2repository"
RUN sdkmanager "extras;google;google_play_services"

# android google apis
RUN sdkmanager "add-ons;addon-google_apis-google-23"

ENV ANDROID_SDK_HOME $ANDROID_HOME
ENV GRADLE_OPTS '-Dorg.gradle.jvmargs="-Xmx2g -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8"'

# Clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN apt-get clean
