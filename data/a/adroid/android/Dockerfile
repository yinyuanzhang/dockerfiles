FROM debian

MAINTAINER Artur Trofymchuk "artur@trofymchuk.net" & Andrew Miroshnychenko "miroshnychenkoandrew@gmail.com"

# Install Deps
RUN apt-get --quiet update --yes

RUN echo deb http://http.debian.net/debian jessie-backports main >> /etc/apt/sources.list
RUN echo deb http://archive.ubuntu.com/ubuntu trusty main universe >> /etc/apt/sources.list

# A few problems with compiling Java from source:
#  1. Oracle.  Licensing prevents us from redistributing the official JDK.
#  2. Compiling OpenJDK also requires the JDK to be installed, and it gets
#       really hairy.

RUN apt-get update && apt-get install -y --no-install-recommends \
		wget \
		tar \
		git \
		unzip \
		lib32stdc++6 \
		lib32z1 \
		bzip2 \
		xz-utils \
	&& rm -rf /var/lib/apt/lists/*

RUN echo 'deb http://deb.debian.org/debian jessie-backports main' > /etc/apt/sources.list.d/jessie-backports.list

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

# add a simple script that can auto-detect the appropriate JAVA_HOME value
# based on whether the JDK or only the JRE is installed
RUN { \
		echo '#!/bin/sh'; \
		echo 'set -e'; \
		echo; \
		echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
	} > /usr/local/bin/docker-java-home \
	&& chmod +x /usr/local/bin/docker-java-home

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

ENV JAVA_VERSION 8u121
ENV JAVA_DEBIAN_VERSION 8u121-b13-1~bpo8+1

# see https://bugs.debian.org/775775
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872
ENV CA_CERTIFICATES_JAVA_VERSION 20161107~bpo8+1

RUN set -x \
	&& apt-get update \
	&& apt-get install -y --force-yes \
		openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \
		ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \
	&& rm -rf /var/lib/apt/lists/* \
	&& [ "$JAVA_HOME" = "$(docker-java-home)" ]

# see CA_CERTIFICATES_JAVA_VERSION notes above
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure

# If you're reading this and have any feedback on how this image could be
#   improved, please open an issue or a pull request so we can discuss it!

RUN update-alternatives --config java
RUN java -version

# Install Android SDK
RUN cd /opt && wget --output-document=android-sdk.tgz --quiet http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && tar xzf android-sdk.tgz && rm -f android-sdk.tgz && chown -R root.root android-sdk-linux

# Setup environment
ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools

# Install sdk elements
ENV PATH ${PATH}:/opt/tools
RUN echo y | android --silent update sdk --no-ui --all --filter platform-tools
#RUN echo y | android --silent update sdk --no-ui --all --filter tools
RUN echo y | android --silent update sdk --no-ui --all --filter extra
RUN echo y | android --silent update sdk --no-ui --all --filter build-tools-25.0.2
RUN echo y | android --silent update sdk --no-ui --all --filter android-25,android-22
RUN echo y | android --silent update sdk --no-ui --all --filter sys-img-armeabi-v7a-android-22
RUN mkdir "$ANDROID_HOME/licenses" || true
RUN echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" > "$ANDROID_HOME/licenses/android-sdk-license"
RUN echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" > "$ANDROID_HOME/licenses/android-sdk-preview-license"
RUN echo y | android update sdk --filter "extra-android-m2repository" --no-ui -a # Grab the Android Support Repo which isn't included in the container

#install gradle
#version 3.2
RUN cd /opt && wget --quiet --output-document=gradle.zip https://services.gradle.org/distributions/gradle-3.2-bin.zip && unzip -q gradle.zip && rm -f gradle.zip && chown -R root.root /opt/gradle-3.2/bin
ENV PATH ${PATH}:/opt/gradle-3.2/bin
# version 3.3
RUN cd /opt && wget --quiet --output-document=gradle.zip https://services.gradle.org/distributions/gradle-3.3-bin.zip && unzip -q gradle.zip && rm -f gradle.zip && chown -R root.root /opt/gradle-3.3/bin
ENV PATH ${PATH}:/opt/gradle-3.3/bin

# Set up and run emulator
RUN android list targets
RUN echo no | android create avd --force -n test -c 30M -t android-22 --abi "default/armeabi-v7a"
ENV HOME /root

ADD wait-for-emulator.sh /usr/local/bin/
ADD start-emulator.sh /usr/local/bin/

RUN which java
RUN which android
RUN which git
RUN which gradle
RUN which adb


# Cleaning
RUN apt-get clean

# GO to workspace
RUN mkdir -p /opt/workspace
VOLUME /root/.gradle
WORKDIR /opt/workspace