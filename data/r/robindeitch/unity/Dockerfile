FROM ubuntu:16.04

ARG DOWNLOAD_URL=https://beta.unity3d.com/download/cef3e6c0c622/UnitySetup-2018.2.20f1
ARG COMPONENTS=Unity,Android

ENV ANDROID_HOME /opt/android-sdk
ENV ANDROID_NDK_HOME /opt/android-ndk
ENV ANDROID_NDK_VERSION r10e

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV PATH ${PATH}:${JAVA_HOME}/jre/bin

ARG DEBIAN_FRONTEND=noninteractive
ARG DEBIAN_FRONTEND=teletype


RUN apt-get update -y && \
  apt-get install -y --no-install-recommends apt-utils

RUN apt-get install -y \
  software-properties-common \
  gconf-service \
  lib32gcc1 \
  lib32stdc++6 \
  libasound2 \
  libarchive13 \
  libc6 \
  libc6-i386 \
  libcairo2 \
  libcap2 \
  libcups2 \
  libdbus-1-3 \
  libexpat1 \
  libfontconfig1 \
  libfreetype6 \
  libgcc1 \
  libgconf-2-4 \
  libgdk-pixbuf2.0-0 \
  libgl1-mesa-glx \
  libglib2.0-0 \
  libglu1-mesa \
  libgtk2.0-0 \
  libgtk3.0 \
  libnspr4 \
  libnss3 \
  libpango1.0-0 \
  libsoup2.4-1 \
  libstdc++6 \
  libx11-6 \
  libxcomposite1 \
  libxcursor1 \
  libxdamage1 \
  libxext6 \
  libxfixes3 \
  libxi6 \
  libxrandr2 \
  libxrender1 \
  libxtst6 \
  zlib1g \
  debconf \
  npm \
  xvfb \
  wget

RUN add-apt-repository ppa:openjdk-r/ppa && \
  apt-get update && \
  apt-get install -y \
  openjdk-8-jdk \
  unzip


# newer SDK versions https://stackoverflow.com/questions/37505709/how-do-i-download-the-android-sdk-without-downloading-android-studio
RUN cd /opt && \
    wget -q https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip -O android-sdk-linux.zip && \
    unzip -q android-sdk-linux.zip -d android-sdk && \
    rm -f android-sdk-linux.zip && \
    ls -ahl android-sdk

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/build-tools

RUN chmod -R 755 .${ANDROID_HOME}/tools/*

# ------------------------------------------------------ 
# --- Install Android SDKs and other build packages 
# https://developer.android.com/studio/command-line/sdkmanager

# platform-tools,extra-android-support
RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager "platform-tools"
RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager "platforms;android-28"
RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager "build-tools;28.0.3"

# accept license
RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses


#  # ------------------------------------------------------
#  # --- Android NDK
#  # download
#  RUN mkdir /opt/android-ndk-tmp && \
#      cd /opt/android-ndk-tmp && \
#      wget -q https://dl.google.com/android/repository/android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip && \
#  # uncompress
#      unzip -q android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip && \
#  # move to its final location
#      mv ./android-ndk-${ANDROID_NDK_VERSION} ${ANDROID_NDK_HOME} && \
#  # remove temp dir
#      cd ${ANDROID_NDK_HOME} && \
#      rm -rf /opt/android-ndk-tmp
#  # add to PATH
#  ENV PATH ${PATH}:${ANDROID_NDK_HOME}

# Unity install ...
RUN wget -nv ${DOWNLOAD_URL} -O UnitySetup && \
  # make executable
  chmod +x UnitySetup && \
  # agree with license
  echo y | \
  # install unity with required components
  ./UnitySetup --unattended \
  --install-location=/opt/Unity \
  --download-location=/tmp/unity \
  --components=$COMPONENTS && \
  # remove setup
  rm -f UnitySetup && \
  # make a directory for the certificate Unity needs to run
  mkdir -p $HOME/.local/share/unity3d/Certificates/

ADD CACerts.pem $HOME/.local/share/unity3d/Certificates/

# --- Cleanup and rev num
RUN apt-get clean autoclean && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

# Clean up
RUN rm -rf /tmp/* /var/tmp/*

RUN df -h
