# https://github.com/bitrise-docker/android/blob/master/Dockerfile
FROM ubuntu:bionic

RUN apt-get update -qq && apt-get install -y -qq cmake swig python2.7 python3 curl zip unzip

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk libc6 libstdc++6 libgcc1 libncurses5 libz1 wget unzip

ENV ANDROID_HOME /opt/android-sdk-linux

# ------------------------------------------------------
# --- Download Android SDK tools into $ANDROID_HOME

RUN cd /opt \
    && wget -q https://dl.google.com/android/repository/android-ndk-r16b-linux-x86_64.zip -O android-sdk-tools.zip \
    && unzip -q android-sdk-tools.zip -d ${ANDROID_HOME} \
    && rm android-sdk-tools.zip

    
ENV SDK android-ndk-r17c

ENV PATH ${PATH}:${ANDROID_HOME}/${SDK}
