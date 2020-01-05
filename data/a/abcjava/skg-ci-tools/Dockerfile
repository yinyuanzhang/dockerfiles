FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive


# The basics (UPDATE, install git and other basic stuff)
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y tzdata && ln -fs /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime && dpkg-reconfigure --frontend noninteractive tzdata && \
    apt-get -y install curl netcat software-properties-common && \
    apt-add-repository ppa:git-core/ppa && \
    apt-get update && \
    apt-get install -y libunwind8 libcurl4 git gosu && \
    rm -rf /var/lib/apt/lists/* && \
    echo "export TERM=xterm" >> /etc/bash.bashrc


# JAVA
ENV JAVA_OPTS=-Xmx5g
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    rm -rf /var/lib/apt/lists/*


# Maven
RUN apt-get update && \
    apt-get install -y maven && \
    rm -rf /var/lib/apt/lists/*


# SBT
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/sbt/bin
ENV SBT_VERSION=1.2.8
ENV SCALA_VERSION=2.12.8
ENV SBT_HOME=/usr/local/sbt
RUN \
    curl -L -o sbt-$SBT_VERSION.deb http://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
    dpkg -i sbt-$SBT_VERSION.deb && \
    rm sbt-$SBT_VERSION.deb && \
    apt-get update && \
    apt-get install sbt && \
    rm -rf /var/lib/apt/lists/*

VOLUME /root/.ivy2
VOLUME /root/.sbt


# NodeJS
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get update && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*


# Xvfb and Google Chrome
RUN curl -sL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y xvfb google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*


# VNC to check on the X Window
RUN apt-get update && \
    apt-get install -y x11vnc && \
    rm -rf /var/lib/apt/lists/*
EXPOSE 5900


# Docker client
WORKDIR /opt
RUN wget https://get.docker.com/builds/Linux/x86_64/docker-1.13.0.tgz && \
    tar -zxvf docker-1.13.0.tgz && \
	rm docker-1.13.0.tgz && \
    ls /opt/docker && \
    mv /opt/docker/docker /usr/local/bin/docker


# swagger2markup
RUN wget https://jcenter.bintray.com/io/github/swagger2markup/swagger2markup-cli/1.3.1/swagger2markup-cli-1.3.1.jar


# Golang
ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH
RUN apt-get update -y && \
    apt-get install -y golang && \
	rm -rf /var/lib/apt/lists/* && \
	mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"

# Google Drive client
RUN go get github.com/prasmussen/gdrive && \
    go install github.com/prasmussen/gdrive

# SSH config - prevents ssh commands from asking for host fingerprint verification - which is not handy when running an automated CI proces
RUN echo "    StrictHostKeyChecking no" >> /etc/ssh/ssh_config
