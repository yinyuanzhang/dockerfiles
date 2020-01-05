FROM golang:1.7.0
MAINTAINER Nuts Project, LLC

RUN go get -u github.com/coreos/clair/contrib/analyze-local-images

RUN echo "deb http://apt.dockerproject.org/repo debian-jessie main" \
        > /etc/apt/sources.list.d/docker.list \
    && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \
        --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
    && apt-get update \
    && apt-get install -y apt-transport-https \
    && apt-get install -y sudo \
    && apt-get install -y docker-engine \
    && rm -rf /var/lib/apt/lists/*
