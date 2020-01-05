FROM phusion/baseimage:0.9.16

MAINTAINER alan.gibson@kapsch.net

ENV VERSION 5.2.4

# Update base OS
RUN apt-get update; \
    apt-get upgrade -y -qq; \
    apt-get install -y -qq sysstat;

# Install Oracle Java 7
RUN \
  echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections; \
  add-apt-repository -y ppa:webupd8team/java; \
  sudo apt-get update; \
  apt-get install -y oracle-java7-installer;

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Download and extract DataStax OpsCenter Agent
RUN mkdir /opt/agent; \
    curl http://downloads.datastax.com/community/datastax-agent-${VERSION}.tar.gz \
    | tar xzf - --strip-components=1 -C "/opt/agent";

ADD	. /src

# Copy over DataStax Agent daemon
RUN	mkdir -p /etc/service/agent; \
    cp /src/agent-run /etc/service/agent/run; \
    chmod u+x /etc/service/agent/run;

WORKDIR /opt/agent

CMD ["/sbin/my_init"]

