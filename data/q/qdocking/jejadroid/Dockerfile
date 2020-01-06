FROM jenkins/jenkins:lts

ENV ANDROID_HOME /opt/android-sdk-linux
ENV ANDROID_SDK_URL https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip

USER root

RUN DEBIAN_FRONTEND=noninteractive apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y ca-certificates wget curl git zip unzip \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y maven gradle make \
 && mkdir -p ${ANDROID_HOME} \
 && cd ${ANDROID_HOME} \
 && wget ${ANDROID_SDK_URL} -O android_tools.zip \
 && unzip android_tools.zip \
 && rm android_tools.zip

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools

RUN yes | sdkmanager --licenses \
 && chown jenkins:jenkins ${ANDROID_HOME} -R

USER jenkins
