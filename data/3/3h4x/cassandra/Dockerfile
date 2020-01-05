FROM abh1nav/java7

MAINTAINER Marcin Branski <ochach@gmail.com>

RUN apt-get update
RUN apt-get install -qy python dnsutils

# Download and extract Cassandra
RUN \
  mkdir /opt/cassandra; \
  wget -O - http://www.us.apache.org/dist/cassandra/2.1.3/apache-cassandra-2.1.3-bin.tar.gz \
  | tar xzf - --strip-components=1 -C "/opt/cassandra";

ADD . /src

# Copy over daemons
RUN cp /src/cassandra.yaml /opt/cassandra/conf/
RUN mkdir -p /etc/service/cassandra
RUN cp /src/cassandra-run /etc/service/cassandra/run

# Expose ports
EXPOSE 7199 7000 7001 9160 9042

WORKDIR /opt/cassandra

CMD ["/sbin/my_init"]

VOLUME ["/opt/cassandra/data"]

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
