FROM ubuntu:18.04
MAINTAINER developers@khipu.com

RUN apt-get update && apt-get upgrade -y \
    && apt-get install curl docker.io zip unzip git openjdk-8-jdk locales maven -y

RUN curl -fsSL https://clis.cloud.ibm.com/install/linux | sh \
    && ibmcloud plugin install container-registry -r Bluemix

RUN curl -fsSL "https://get.sdkman.io" | bash

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

