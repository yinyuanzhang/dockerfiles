FROM niah9119/docker-raspberrypi3

MAINTAINER Niclas Ahlstrand <niclas.ahlstrand@gmail.com>

RUN [ "cross-build-start" ]

RUN apt-get install unzip

ADD h2*.zip /tmp/

# Install H2
RUN  unzip /tmp/h2-*.zip -d /tmp
RUN  rm -f h2-*.zip
RUN  mkdir -p /opt/h2
RUN  mv /tmp/h2 /opt/
RUN  mkdir -p /opt/h2-data
RUN  rm -f /tmp/h2*.zip

RUN [ "cross-build-end" ]

VOLUME /opt/h2-data

# Expose ports.
#   - 1521: H2 Server
#   - 9090: H2 Console
EXPOSE 1521 9090

# Define default command
CMD java -cp /opt/h2/bin/h2*.jar org.h2.tools.Server -web -webAllowOthers -webPort 9090 -tcp -tcpAllowOthers -tcpPort 1521 -baseDir /opt/h2-data
