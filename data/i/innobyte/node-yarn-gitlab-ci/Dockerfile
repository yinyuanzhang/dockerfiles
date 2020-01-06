FROM node:10
MAINTAINER Alin Alexandru <alin.alexandru@innobyte.com>
MAINTAINER Cosmin Petrescu <cosmin.petrescu@innobyte.com>

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get -y autoremove && \
    apt-get clean

RUN apt-get install -y zip

RUN export CLOUD_SDK_REPO="cloud-sdk" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update -y && apt-get install google-cloud-sdk -y

RUN \
    apt-get update \
    && apt-get install -y --no-install-recommends \
    python \
    python-dev \
    python-pip \
    python-yaml \
    && apt-get clean

RUN pip install awscli

RUN npm install -g cordova cordova-icon cordova-splash firebase-tools
