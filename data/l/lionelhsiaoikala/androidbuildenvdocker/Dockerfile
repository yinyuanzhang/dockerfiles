FROM openjdk:8-jdk-slim

ENV SDK_URL="https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip" \
    ANDROID_HOME="/usr/local/android-sdk" \
    ANDROID_VERSION=29 \
    ANDROID_BUILD_TOOLS_VERSION=29.0.2

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        unzip && \
    javac -version && \
    mkdir "$ANDROID_HOME" .android && \
    cd "$ANDROID_HOME" && \
    curl -o sdk.zip $SDK_URL && \
    unzip sdk.zip && \
    rm sdk.zip && \
    yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses && \
    $ANDROID_HOME/tools/bin/sdkmanager --update && \
    $ANDROID_HOME/tools/bin/sdkmanager \
        "build-tools;${ANDROID_BUILD_TOOLS_VERSION}" \
        "platforms;android-${ANDROID_VERSION}" \
        "platform-tools" && \
    apt-get remove -y \
        curl \
        unzip && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /tmp/* && \
    mkdir /application

WORKDIR /application
