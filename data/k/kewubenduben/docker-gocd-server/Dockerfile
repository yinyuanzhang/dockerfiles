FROM ubuntu:trusty
MAINTAINER Ker Ruben Ramos, kerruben@yahoo.com

RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    openjdk-7-jre-headless \
    unzip \
    wget \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

RUN wget -O /tmp/go-server.deb http://download.go.cd/gocd-deb/go-server-14.4.0-1356.deb
RUN dpkg -i /tmp/go-server.deb
RUN rm /tmp/go-server.deb

EXPOSE 8153
EXPOSE 8154

CMD ["/etc/init.d/go-server", "start"]
CMD /etc/init.d/go-server start && tail -f /var/log/go-server/go-server.log