###########################################
##  Google App Engine go1.12
##   - gcloud 262.0.0
###########################################
FROM ubuntu:18.04
MAINTAINER @eaglesakura

ARG GCLOUD_INSTALL_VERSION="271.0.0"
ARG GCLOUD_DOWNLOAD_URL=https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-207.0.0-linux-x86_64.tar.gz
ARG GOLANG_VERSION=1.12.13
ENV DEBIAN_FRONTEND=noninteractive

RUN  apt update \
  && mkdir $HOME/tools \
  && apt install -y jq python git wget curl unzip tzdata build-essential

###########################################
## Install gcloud tools
###########################################
ENV PATH="/root/tools/google-cloud-sdk/bin:/root/tools/google-cloud-sdk/platform/google_appengine:/root/tools/google-cloud-sdk/platform/google_appengine/goroot-1.9/bin:/root/tools/google-cloud-sdk/platform/google_appengine/dev_appserver.py:/root/tools/google-cloud-sdk/platform/google_appengine/endpointscfg.py:$PATH"
RUN  cd $HOME/tools  \
  && wget -O gcloud.tar.gz ${GCLOUD_DOWNLOAD_URL} \
  && tar xovfz gcloud.tar.gz -C $HOME/tools \
  && rm gcloud.tar.gz \
  && yes | ./google-cloud-sdk/install.sh \
  && yes | gcloud components update --version=${GCLOUD_INSTALL_VERSION} \
  && yes | gcloud components install app-engine-go

###########################################
## Install golang
###########################################
ENV PATH="/root/tools/go/bin:/root/tools/gopath/bin:$PATH" \
    GOROOT="/root/tools/go" \
    GOPATH="/root/tools/gopath" \
    GOBIN="/root/tools/gopath/bin"
RUN  mkdir $HOME/tools/gopath \
  && mkdir $HOME/tools/gopath/bin \
  && wget https://storage.googleapis.com/golang/go${GOLANG_VERSION}.linux-amd64.tar.gz -O $HOME/golang.temp.tar.gz \
  && tar xovfz "$HOME/golang.temp.tar.gz" -C "$HOME/tools/" > /dev/null \
  && rm $HOME/golang.temp.tar.gz

RUN  go get -f -u github.com/eaglesakura/cli/gcloud-auth \
  && rm -rf $GOPATH/src \
  && rm -rf $GOPATH/pkg
  