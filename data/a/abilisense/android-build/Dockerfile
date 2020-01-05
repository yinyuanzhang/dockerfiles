FROM openjdk:8-jdk
MAINTAINER Anatoly Tokalov <anttdev@gmail.com>

WORKDIR /opt

ENV ANDROID_TARGET_SDK="24" \
    ANDROID_BUILD_TOOLS="24.0.3" \
    ANDROID_SDK_TOOLS="24.4.1"

RUN apt-get --quiet update --yes
RUN apt-get --quiet install --yes wget tar unzip lib32stdc++6 lib32z1

RUN mkdir android-sdk-linux

RUN wget --quiet --output-document=sdk-tools-linux.zip https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip && \
    unzip sdk-tools-linux.zip -d android-sdk-linux

RUN yes | android-sdk-linux/tools/bin/sdkmanager --licenses
RUN wget -q https://dl.google.com/android/repository/android-ndk-r15c-linux-x86_64.zip -O /tmp/android-ndk-r15c-linux-x86_64.zip && \
	unzip -d /opt/android-sdk-linux/ /tmp/android-ndk-r15c-linux-x86_64.zip && \
	mv /opt/android-sdk-linux/android-ndk-r15c /opt/android-sdk-linux/ndk-bundle

ENV ANDROID_HOME /opt/android-sdk-linux