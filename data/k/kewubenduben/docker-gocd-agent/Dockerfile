FROM ubuntu:trusty
MAINTAINER Ker Ruben Ramos, kerruben@yahoo.com

RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    git \
    mercurial \
    openjdk-7-jre-headless \
    subversion \
    unzip \
    wget \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

RUN wget -O /tmp/go-agent.deb http://download.go.cd/gocd-deb/go-agent-14.4.0-1356.deb
RUN dpkg -i /tmp/go-agent.deb
RUN rm /tmp/go-agent.deb

RUN sed -r -i "s/^(GO_SERVER)=(.*)/\1=\$GO_SERVER_ADDR/g" /etc/default/go-agent

VOLUME ["/var/lib/go-agent"]

CMD /usr/lib/jvm/java-7-openjdk-amd64/bin/java -jar /usr/share/go-agent/agent-bootstrapper.jar $GO_SERVER_ADDR $GO_SERVER_PORT