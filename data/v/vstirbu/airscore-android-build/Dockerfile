FROM ubuntu:16.04
MAINTAINER Vlad Știrbu, vlad@smallthin.gs
LABEL version="1.0.1"
# https://github.com/bitrise-io/bitrise-base/blob/master/Dockerfile

# ------------------------------------------------------
# --- Environments and base directories

# Environments
# - Language
ENV LANG="en_US.UTF-8" \
    LANGUAGE="en_US.UTF-8" \
    LC_ALL="en_US.UTF-8"

# ------------------------------------------------------
# --- Base pre-installed tools
RUN apt-get update -qq

# Generate proper EN US UTF-8 locale
# Install the "locales" package - required for locale-gen
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
    locales \
    # Do Locale gen
    && locale-gen en_US.UTF-8


RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
    curl \
    git \
    sudo \
    wget \
    # Python
    python \
    python-dev \
    python-pip \
    # Common, useful
    build-essential \
    zip \
    unzip \
    tree \
    clang \
    # For PPAs
    software-properties-common

# ------------------------------------------------------
# --- Pre-installed but not through apt-get


# Install NodeJS
#  from official docs: https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN sudo apt-get install -y nodejs


# Android
# https://github.com/bitrise-io/android/blob/master/Dockerfile
ENV ANDROID_HOME /opt/android-sdk-linux


# ------------------------------------------------------
# --- Install required tools

RUN apt-get update -qq

# Dependencies to execute Android builds
RUN dpkg --add-architecture i386
RUN apt-get update -qq
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk libc6:i386 libstdc++6:i386 libgcc1:i386 libncurses5:i386 libz1:i386


# ------------------------------------------------------
# --- Download Android SDK tools into $ANDROID_HOME

RUN cd /opt \
    # && wget -q https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip -O android-sdk-tools.zip \
    && wget -q https://dl.google.com/android/repository/tools_r25.0.5-linux.zip -O android-sdk-tools.zip \
    && unzip -q android-sdk-tools.zip -d ${ANDROID_HOME} \
    && rm android-sdk-tools.zip

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools


# ------------------------------------------------------
# --- Install Android SDKs and other build packages

RUN echo y | android update sdk -a -u -t android-22,build-tools-24.0.3,extra


# ------------------------------------------------------
# --- Install Gradle from PPA

RUN apt-get update \
    && apt-get -y install gradle \
    && gradle -v


# ------------------------------------------------------
# --- Install Maven 3 from PPA

RUN apt-get purge maven maven2 \
    && apt-get update \
    && apt-get -y install maven \
    && mvn --version


# Install Cordova and other global tools

RUN npm install -g cordova@5.4.1
RUN npm install -g cordova-gen-icon@0.4.6
RUN npm install -g cordova-xml


# Application npm install
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
    autoconf \
    libjpeg-dev \
    libpng-dev \
    imagemagick \
    pkg-config


# Cleaning
RUN apt-get clean

