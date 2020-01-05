FROM sstarcher/sensu:1.4.3

ENV CLIENT_NAME="localhost"
ENV CLIENT_ADDRESS="127.0.0.1"
ENV CLIENT_SUBSCRIPTIONS="linux,internet"
ENV TRANSPORT_NAME="rabbitmq"
ENV RABBITMQ_USER="sensu"
ENV RABBITMQ_PASSWORD="sensu"
ENV RABBITMQ_VHOST="/sensu"


USER root

RUN apt-get update -y &&\
    apt-get install -y make gcc g++ python wget libc-dev
RUN sensu-install -p influxdb &&\
    sensu-install -p cpu-checks &&\
    sensu-install -p disk-checks &&\
    sensu-install -p memory-checks &&\
    sensu-install -p uptime-checks &&\
    sensu-install -p network-checks &&\
    sensu-install -p io-checks &&\
    sensu-install -p filesystem-checks &&\
    sensu-install -p process-checks &&\
    sensu-install -p filesystem-checks &&\
    sensu-install -p vmstats &&\
    sensu-install -p logs &&\
    sensu-install -p dns &&\
    sensu-install -p docker &&\
    sensu-install -p http &&\
    sensu-install -p mailer &&\
    sensu-install -p postfix

RUN wget -O /usr/local/bin/speedtest-cli https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py &&\
    chmod +x /usr/local/bin/speedtest-cli

RUN cp /usr/local/bundle/gems/sensu-plugins-influxdb-2.0.0/bin/* \
    /usr/local/bundle/gems/sensu-plugins-mailer-4.0.0/bin/* \
    /etc/sensu/extensions/

COPY files/extensions /etc/sensu/extensions
COPY files/conf.d /etc/sensu/conf.d
COPY files/check.d /etc/sensu/check.d
COPY files/handlers /etc/sensu/handlers

RUN chmod 755 /etc/sensu/extensions/*

RUN chown -R sensu:sensu /etc/sensu/conf.d /etc/sensu/check.d /etc/sensu/handlers /etc/sensu/extensions/