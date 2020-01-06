FROM debian:wheezy

RUN groupadd -r rabbitmq && useradd -r -d /var/lib/rabbitmq -m -g rabbitmq rabbitmq \
    && apt-get update && apt-get install -y curl redis-server supervisor git \
    && curl http://packages.erlang-solutions.com/debian/erlang_solutions.asc | apt-key add - \
    && echo "deb http://packages.erlang-solutions.com/debian wheezy contrib" | tee /etc/apt/sources.list.d/erlang.list \
    && curl http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add - \
    && echo "deb http://www.rabbitmq.com/debian/ testing main" | tee /etc/apt/sources.list.d/rabbitmq.list \
    && curl http://repos.sensuapp.org/apt/pubkey.gpg | apt-key add - \
    && echo "deb http://repos.sensuapp.org/apt sensu main" | tee /etc/apt/sources.list.d/sensu.list \
    && apt-get update && apt-get install -y rabbitmq-server sensu \
    && echo '[{rabbit, [{loopback_users, []}]}].' > /etc/rabbitmq/rabbitmq.config \
    && mkdir -p /tmp/sensu && cd /tmp/sensu \
    && git clone https://github.com/sensu/sensu-community-plugins.git /tmp/sensu/plugin \
    && cp -rpf /tmp/sensu/plugin/plugins/* /etc/sensu/plugins/ \
    && chown -R sensu /etc/sensu/plugins/ && chmod -R 755 /etc/sensu/plugins/ \
    && mkdir -p /var/log/sensu && chown -R sensu /var/log/sensu && chmod 755 -R /var/log/sensu \
    && curl -L -o uchiwa.deb http://dl.bintray.com/palourde/uchiwa/uchiwa_0.9.1-1_amd64.deb \
    && dpkg -i uchiwa.deb \
    && apt-get --purge autoremove -y curl git && apt-get clean \
    && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

COPY sensu /etc/sensu
COPY rabbitmq /etc/rabbitmq
COPY redis/redis.conf /etc/redis/redis.conf
COPY entrypoint.conf /etc/entrypoint.conf

WORKDIR /var/lib/rabbitmq

ENV PATH $PATH:/etc/sensu/plugins:/etc/sensu/handlers

EXPOSE 3000 4567 5672 6379

ENTRYPOINT ["/usr/bin/supervisord", "-a", "1024", "-c", "/etc/entrypoint.conf"]