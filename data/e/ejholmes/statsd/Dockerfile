FROM ubuntu:12.04
MAINTAINER Eric Holmes <eric@ejholmes.io>

ADD ./bin/build /bin/build
RUN /bin/build
ADD ./config.js /opt/statsd/

WORKDIR /opt/statsd

EXPOSE 8125/udp
EXPOSE 8126

ENTRYPOINT ["node", "stats.js", "config.js"]
