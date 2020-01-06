FROM node:0.10
MAINTAINER Eloy Coto <eloy.coto@gmail.com>

RUN git clone https://github.com/etsy/statsd.git /statsd && \
    cd statsd && \
    npm install statsd-influxdb-backend

ADD config.js /statsd/

EXPOSE 8125
WORKDIR /statsd/
ENTRYPOINT [ "node", "stats.js", "config.js" ]
