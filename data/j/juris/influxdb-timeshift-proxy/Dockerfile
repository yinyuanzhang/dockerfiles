FROM node:11.9.0-alpine

ENV INFLUXDB=influxdb:8086

WORKDIR /usr/src/influxdb-timeshift-proxy

ADD https://github.com/maxsivanov/influxdb-timeshift-proxy/archive/master.zip .

RUN unzip master.zip \
    && mv influxdb-timeshift-proxy-master/* . \
    && rm -fr master.zip influxdb-timeshift-proxy-master \
    && npm i \
    && npm audit fix --force

EXPOSE 8089

CMD exec npm run start
