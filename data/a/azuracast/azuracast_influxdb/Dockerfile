FROM influxdb:1.6-alpine

RUN apk add --no-cache bash

COPY ./scripts/import_folder /usr/bin/import_folder

RUN chmod a+x /usr/bin/import_folder

ENV INFLUXDB_BIND_ADDRESS=0.0.0.0:8088
EXPOSE 8088