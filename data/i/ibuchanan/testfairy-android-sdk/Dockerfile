FROM atlassian/default-image:latest
MAINTAINER support@testfairy.com

ENV ANT_VERSION 1.9.4
ENV ANDROID_SDK_VERSION 24.4.1

# Prepare platform, basic stuff like "curl"
RUN \
	df -kh && \
	dpkg --add-architecture i386 && \
	apt-get update -y && \
	apt-get install -y curl

# Install Oracle JDK 7
RUN \
	apt-get install -y software-properties-common && \
	add-apt-repository ppa:webupd8team/java -y && \
	apt-get update -y && \
	echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
	apt-get install -y oracle-java7-installer && \
	apt-get remove software-properties-common -y && \
	apt-get autoremove -y && \
	apt-get clean

ENV JAVA_HOME /usr/lib/jvm/java-7-oracle

# Install Apache ANT
RUN \
	cd /usr/local/ && \
	curl -sL https://archive.apache.org/dist/ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz | tar xvfz - && \
	mv apache-ant-${ANT_VERSION} /usr/local/ant

ENV ANT_HOME /usr/local/ant

# Install Android SDK
ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/tools:${ANT_HOME}/bin

RUN \
	cd /usr/local && \
	curl -sL https://dl.google.com/android/android-sdk_r${ANDROID_SDK_VERSION}-linux.tgz | tar xvzf - && \
	echo y | android update sdk --no-ui --all --filter platform-tools && \
	echo y | android update sdk --no-ui --all --filter extra-android-support && \
	echo y | android update sdk --no-ui --all --filter android-24 && \
	echo y | android update sdk --no-ui --all --filter android-23 && \
	echo y | android update sdk --no-ui --all --filter android-22 && \
	echo y | android update sdk --no-ui --all --filter android-21 && \
	echo y | android update sdk --no-ui --all --filter android-19 && \
	echo y | android update sdk --no-ui --all --filter android-17 && \
	echo y | android update sdk --no-ui --all --filter build-tools-24.0.2 && \
	echo y | android update sdk --no-ui --all --filter build-tools-24.0.1 && \
	echo y | android update sdk --no-ui --all --filter build-tools-24.0.0 && \
	echo y | android update sdk --no-ui --all --filter build-tools-23.0.3 && \
	echo y | android update sdk --no-ui --all --filter build-tools-23.0.2 && \
	echo y | android update sdk --no-ui --all --filter build-tools-23.0.1 && \
	echo y | android update sdk --no-ui --all --filter build-tools-22.0.1 && \
	echo y | android update sdk --no-ui --all --filter build-tools-22.0.0 && \
	echo y | android update sdk --no-ui --all --filter build-tools-21.1.2 && \
	echo y | android update sdk --no-ui --all --filter build-tools-21.1.1 && \
	echo y | android update sdk --no-ui --all --filter build-tools-21.1.0 && \
	echo y | android update sdk --no-ui --all --filter build-tools-21.0.2 && \
	echo y | android update sdk --no-ui --all --filter build-tools-21.0.1 && \
	echo y | android update sdk --no-ui --all --filter build-tools-21.0.0 && \
	echo y | android update sdk --no-ui --all --filter build-tools-22.0.0 && \
	echo y | android update sdk --no-ui --all --filter build-tools-20.0.0 && \
	echo y | android update sdk --no-ui --all --filter build-tools-19.1.0 && \
	echo y | android update sdk --no-ui --all --filter build-tools-17.0.0 && \
	echo y | android update sdk --no-ui --all --filter extra-android-m2repository && \
	echo y | android update sdk --no-ui --all --filter extra-google-m2repository && \
	echo y | android update sdk --no-ui --all --filter extra-google-google_play_services && \
	echo y | android update sdk --no-ui --all --filter addon-google_apis-google-24 && \
	echo y | android update sdk --no-ui --all --filter addon-google_apis-google-23 && \
	echo y | android update sdk --no-ui --all --filter addon-google_apis-google-22 && \
	echo y | android update sdk --no-ui --all --filter addon-google_apis-google-21 


ENV TERM=dumb
RUN mkdir -p /opt/atlassian/bitbucketci/agent/build
WORKDIR /opt/atlassian/bitbucketci/agent/build
ENTRYPOINT /bin/bash
