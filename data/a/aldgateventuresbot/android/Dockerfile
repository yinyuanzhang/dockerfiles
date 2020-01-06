FROM openjdk:8u181-jdk-stretch

ENV ANDROID_HOME /opt/android-sdk
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools

ADD https://raw.githubusercontent.com/fsaintjacques/semver-tool/master/src/semver /usr/local/bin/semver
ADD https://raw.githubusercontent.com/rockymadden/slack-cli/master/src/slack /usr/local/bin/slack

RUN apt-get update && \
    apt-get install -y openjdk-8-jdk wget unzip curl jq

RUN mkdir -p ${ANDROID_HOME} && \
    cd ${ANDROID_HOME} && \
    wget -q https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip -O android_tools.zip && \
    unzip android_tools.zip

RUN yes | sdkmanager --licenses && \
    chmod +x /usr/local/bin/semver /usr/local/bin/slack && \
    rm -rf /var/lib/apt/lists/* ${ANDROID_HOME}/android_tools.zip
