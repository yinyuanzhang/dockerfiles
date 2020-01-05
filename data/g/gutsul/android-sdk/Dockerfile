FROM openjdk:8-jdk
MAINTAINER Yuriy Grigortsevich <GrigortsevichYuriy@gmail.com>

ENV ANDROID_COMPILE_SDK "27"
ENV ANDROID_BUILD_TOOLS "26.0.2"
ENV ANDROID_SDK_TOOLS "4333796"

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    tar \
    unzip \
    lib32stdc++6 \
    lib32z1 \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# --quiet
RUN wget --output-document=sdk.zip https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_TOOLS}.zip \
 && unzip -d sdk sdk.zip \
 && rm -f sdk.zip
RUN echo y | sdk/tools/bin/sdkmanager "platforms;android-${ANDROID_COMPILE_SDK}"
RUN echo y | sdk/tools/bin/sdkmanager "platform-tools"
RUN echo y | sdk/tools/bin/sdkmanager "build-tools;${ANDROID_BUILD_TOOLS}"

ENV ANDROID_HOME="/sdk"
ENV PATH="$PATH:${ANDROID_HOME}/tools"


  # - export ANDROID_HOME=$PWD/android-sdk-linux
  # - export PATH=$PATH:$PWD/android-sdk-linux/platform-tools/
  # - chmod +x ./gradlew
  # temporarily disable checking for EPIPE error and use yes to accept all licenses
  # - set +o pipefail
  # - yes | android-sdk-linux/tools/bin/sdkmanager --licenses
  # - set -o pipefail
