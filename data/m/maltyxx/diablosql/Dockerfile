FROM debian:jessie

MAINTAINER Yoann Vanitou <yvanitou@gmail.com>

RUN apt-get update \
    && apt-get --yes install \
        php5-cli \
        php5-mysqlnd \
        mysql-client \
        pv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/*

COPY diablosql /opt/diablosql

RUN chmod -v 755 /opt/diablosql/diablosql.sh

COPY ./docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod -v 755 /docker-entrypoint.sh

RUN mkdir -vp \
    /opt/diablosql/conf \
    /opt/diablosql/data \
    /opt/diablosql/log

VOLUME ["/opt/diablosql/conf", "/opt/diablosql/data", "/opt/diablosql/log"]

WORKDIR "/opt/diablosql"

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/opt/diablosql/diablosql.sh"]
