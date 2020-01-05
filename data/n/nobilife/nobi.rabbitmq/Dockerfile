FROM rabbitmq:3.7-management
ADD plugins/rabbitmq_delayed_message_exchange-20171201-3.7.x.ez /plugins/
ADD enabled_plugins /etc/rabbitmq/enabled_plugins
ADD rabbitmq.conf /etc/rabbitmq/rabbitmq.conf

ADD init.sh /init.sh
RUN chmod +x init.sh

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
