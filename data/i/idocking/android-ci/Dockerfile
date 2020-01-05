FROM ubuntu:16.04

ENV VERSION_SDK_TOOLS "3859397"

ENV ANDROID_HOME "/sdk"
ENV PATH "$PATH:${ANDROID_HOME}/tools"
ENV DEBIAN_FRONTEND noninteractive

## For chinese user
# RUN sed -i "s/http:\/\/archive\.ubuntu\.com/http:\/\/mirrors\.aliyun\.com/g" /etc/apt/sources.list

RUN apt-get -qq update && \
    apt-get install -y --no-install-recommends \
      bzip2 \
      git-core \
      html2text \
      openjdk-8-jdk \
      libc6-i386 \
      lib32stdc++6 \
      lib32gcc1 \
      lib32ncurses5 \
      lib32z1 \
      unzip \
      wget \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN rm -f /etc/ssl/certs/java/cacerts; \
    /var/lib/dpkg/info/ca-certificates-java.postinst configure

RUN wget -q https://dl.google.com/android/repository/sdk-tools-linux-${VERSION_SDK_TOOLS}.zip -O /sdk.zip && \
    unzip /sdk.zip -d /sdk && \
    rm -v /sdk.zip

ADD packages.txt /sdk
ADD licenses/ /sdk/licenses

RUN mkdir -p /root/.android && \
  touch /root/.android/repositories.cfg && \
  ${ANDROID_HOME}/tools/bin/sdkmanager --update 

RUN while read -r package; do PACKAGES="${PACKAGES}${package} "; done < /sdk/packages.txt && \
    ${ANDROID_HOME}/tools/bin/sdkmanager ${PACKAGES}