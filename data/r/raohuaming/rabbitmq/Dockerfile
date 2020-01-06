FROM bitnami/rabbitmq:3.7.2-r1

# plugin download page: https://www.rabbitmq.com/community-plugins.html
# download from https://dl.bintray.com/rabbitmq/community-plugins/3.7.x/rabbitmq_delayed_message_exchange/rabbitmq_delayed_message_exchange-20171201-3.7.x.zip
COPY ./rootfs /

RUN rabbitmq-plugins enable rabbitmq_delayed_message_exchange
