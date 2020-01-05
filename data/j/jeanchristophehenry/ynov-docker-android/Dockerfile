# █████╗ ███╗   ██╗██████╗ ██████╗  ██████╗ ██╗██████╗     ██████╗ ███████╗██╗   ██╗
#██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██║██╔══██╗    ██╔══██╗██╔════╝██║   ██║
#███████║██╔██╗ ██║██║  ██║██████╔╝██║   ██║██║██║  ██║    ██║  ██║█████╗  ██║   ██║
#██╔══██║██║╚██╗██║██║  ██║██╔══██╗██║   ██║██║██║  ██║    ██║  ██║██╔══╝  ╚██╗ ██╔╝
#██║  ██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║██████╔╝    ██████╔╝███████╗ ╚████╔╝
#╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝     ╚═════╝ ╚══════╝  ╚═══╝
#
#██████╗ ███████╗ █████╗  ██████╗████████╗    ███╗   ██╗ █████╗ ████████╗██╗██╗   ██╗███████╗
#██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝    ████╗  ██║██╔══██╗╚══██╔══╝██║██║   ██║██╔════╝
#██████╔╝█████╗  ███████║██║        ██║       ██╔██╗ ██║███████║   ██║   ██║██║   ██║█████╗
#██╔══██╗██╔══╝  ██╔══██║██║        ██║       ██║╚██╗██║██╔══██║   ██║   ██║╚██╗ ██╔╝██╔══╝
#██║  ██║███████╗██║  ██║╚██████╗   ██║       ██║ ╚████║██║  ██║   ██║   ██║ ╚████╔╝ ███████╗
#╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝       ╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝  ╚══════╝
#
# Pull base image.
FROM ubuntu:18.04

# extra metadata
MAINTAINER Jean-Christophe HENRY < jean.christophe.henry.pro[at]gmail.com >

# extra metadata
LABEL version="1.0"
LABEL Description="This image provides a base Android development environment for React Native and fastlane, and may be used to run tests, and use gitlab-ci."

# ——————————
# Configure timezone and locale

# RUN export LANGUAGE=en_US.UTF-8
# RUN export LANG=en_US.UTF-8
# RUN export LC_ALL=en_US.UTF-8
# RUN echo "Europe/Paris" > /etc/timezone && \
#        echo 'LANG="fr_FR.UTF-8"'>/etc/default/locale && \
#      dpkg-reconfigure --frontend=noninteractive locales && \
#        update-locale LANG=fr_FR.UTF-8

RUN apt-get update && apt-get install -y locales

RUN echo "Europe/Paris" > /etc/timezone
RUN locale-gen --purge en_US.UTF-8
RUN echo -e 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' > /etc/default/locale

# ——————————
# Essentials

RUN apt-get install -y \
      curl \
      wget \
      git \
      build-essential \
      && apt-get clean

# ——————————
# Java
RUN apt-get install -y openjdk-8-jdk

# ——————————
# Ruby
RUN apt-get install -y ruby-full && \
      gem install --no-rdoc --no-ri bundler

# ——————————
# Node
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

# Yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y yarn


# ——————————
# React Native
RUN npm install -g react-native-cli

# ——————————
# Android

ENV ANDROID_HOME /opt/android-sdk-linux
ENV ANDROID_SDK_TOOLS_FILENAME sdk-tools-linux-3859397.zip
ENV ANDROID_SDK_TOOLS_URL https://dl.google.com/android/repository/${ANDROID_SDK_TOOLS_FILENAME}
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/23.0.1

# Install just the SDK tools
RUN mkdir -p ${ANDROID_HOME}
RUN cd /opt && \
    wget -q ${ANDROID_SDK_TOOLS_URL} && \
    unzip -n ${ANDROID_SDK_TOOLS_FILENAME} -d android-sdk-linux && \
    rm ${ANDROID_SDK_TOOLS_FILENAME}

# Accept those licenses, then install packages
RUN yes | sdkmanager --licenses
RUN sdkmanager \
      "build-tools;23.0.1" \
      "build-tools;23.0.3" \
      "build-tools;25.0.1" \
      "build-tools;25.0.2" \
      "emulator" \
      "extras;android;m2repository" \
      "extras;google;m2repository" \
      "patcher;v4" \
      "platform-tools" \
      "platforms;android-23" \
      "platforms;android-25" \
      "tools"

# Gradle
ENV GRADLE_VERSION 2.14.1
ENV GRADLE_HOME /usr/bin/gradle
ENV PATH $PATH:$GRADLE_HOME/bin

RUN cd /usr/lib && \
      curl --verbose -fl https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip -o gradle-all.zip && \
      unzip /usr/lib/gradle-all.zip && \
      ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" $GRADLE_HOME && \
      rm /usr/lib/gradle-all.zip

# ———————————————————————————————————
# Installation fastlane and add plugin
RUN gem install fastlane -NV \
  && gem install fastlane-plugin-appicon fastlane-plugin-increment_version_code fastlane-plugin-humanable_build_number \
  && gem update --system

# i386 architecture required for running 32 bit Android tools
RUN dpkg --add-architecture i386 && \
      apt-get update -y && \
      apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 && \
      rm -rf /var/lib/apt/lists/* && \
      apt-get autoremove -y && \
      apt-get clean

# Output versions
RUN node -v && npm -v && ruby -v && fastlane -v
