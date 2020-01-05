FROM rabbitmq:3.7.4-management

RUN \
    apt-get update \
    && apt-get -y install gettext-base \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY config/* /etc/rabbitmq/

RUN chown -R rabbitmq:rabbitmq /etc/rabbitmq

CMD ["rabbitmq-server", "-config", "/etc/rabbitmq/advanced.config"]

EXPOSE 61613

COPY docker-entrypoint.coyo.sh /usr/local/bin/docker-entrypoint.coyo.sh

ENV DISK_FREE_LIMIT "50000000"

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.coyo.sh"]
