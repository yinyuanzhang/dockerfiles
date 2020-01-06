FROM alpine

RUN apk update \
    && apk add ca-certificates wget \
    && update-ca-certificates

COPY id.config /var/id.config
COPY core.config /var/core.config
COPY services.json /var/services.json
COPY businesshours.json /var/businesshours.json
COPY network.config /var/network.config
COPY bin/qsynccore /var/qsynccore
COPY run.sh /var/run.sh

EXPOSE 5000

WORKDIR /var
CMD [ "/bin/sh", "/var/run.sh" ]