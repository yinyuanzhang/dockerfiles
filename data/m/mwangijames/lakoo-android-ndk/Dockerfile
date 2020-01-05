FROM openjdk:8-jdk
MAINTAINER James Mwangi <james@dukaconnect.com>

RUN mkdir -p /opt/android-sdk-linux && mkdir -p ~/.android && touch ~/.android/repositories.cfg
WORKDIR /opt

ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools:${PATH}:${ANDROID_HOME}/tools
ENV ANDROID_NDK /opt/android-ndk-linux
ENV ANDROID_NDK_HOME /opt/android-ndk-linux

RUN apt-get -qq update && \
	apt-get install -qqy --no-install-recommends \
	build-essential \
  file \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN apt-get update && apt-get install -y --no-install-recommends \
	unzip \
	wget
RUN cd /opt/android-sdk-linux && \
	wget -q --output-document=sdk-tools.zip https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip && \
	unzip sdk-tools.zip && \
	rm -f sdk-tools.zip && \
	echo y | sdkmanager "build-tools;25.0.3" "platforms;android-26" && \
	echo y | sdkmanager "extras;android;m2repository" "extras;google;m2repository" "extras;google;google_play_services" && \
	sdkmanager "cmake;3.6.4111459" && \
  yes | sdkmanager --licenses  
RUN wget -q --output-document=android-ndk.zip https://dl.google.com/android/repository/android-ndk-r15c-linux-x86_64.zip && \
	unzip android-ndk.zip && \
	rm -f android-ndk.zip && \
	mv android-ndk-r15c android-ndk-linux
