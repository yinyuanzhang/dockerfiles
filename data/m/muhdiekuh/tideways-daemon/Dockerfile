#FROM ubuntu:xenial
FROM phusion/baseimage:0.11
COPY EEB5E8F4.gpg /tmp/EEB5E8F4.gpg
RUN echo 'deb http://s3-eu-west-1.amazonaws.com/tideways/packages debian main' > /etc/apt/sources.list.d/tideways.list && \
    apt-key add /tmp/EEB5E8F4.gpg && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -yq install tideways-daemon && \
    apt-get autoremove --assume-yes && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 9135
EXPOSE 8135/udp


ENV TIDEWAYS_HOSTNAME=tideways-daemon
ENV TIDEWAYS_ENVIRONMENT=production

CMD ["sh", "-c",  "/usr/bin/tideways-daemon --hostname=${TIDEWAYS_HOSTNAME} --address=0.0.0.0:9135 --udp=0.0.0.0:8135 --env=$TIDEWAYS_ENVIRONMENT"]


