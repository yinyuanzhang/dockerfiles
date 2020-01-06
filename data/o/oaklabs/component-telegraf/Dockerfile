FROM telegraf:1.9.5

USER root

WORKDIR /

COPY config/ /
COPY secrets /secrets
COPY entrypoint.sh /

RUN chmod -R 0400 /secrets \
    && chown -R root:root /secrets \
    && chmod +x /entrypoint.sh

ENV INFLUXDB_HOST="http://influxdb.oak.host:8086" \
    GOOGLE_ZONE="us-east1-b" \
    GOOGLE_APPLICATION_CREDENTIALS="/secrets/default-credentials.json" \
    AWS_TOKEN='' \
    BUCKET='' \
    INFLUXDB_ORG=''

ENTRYPOINT [ "/entrypoint.sh" ]