FROM rabbitmq:3.7.14-management

COPY docker-healthcheck ./usr/local/bin/

RUN apt-get update && \
    apt-get install -y curl unzip

# install delaymed message exchange plugin
RUN curl https://dl.bintray.com/rabbitmq/community-plugins/3.7.x/rabbitmq_delayed_message_exchange/rabbitmq_delayed_message_exchange-20171201-3.7.x.zip > rabbitmq_delayed_message_exchange-20171201-3.7.x.zip && \
    unzip rabbitmq_delayed_message_exchange-20171201-3.7.x.zip && \
    rm -f rabbitmq_delayed_message_exchange-20171201-3.7.x.zip && \
    mv rabbitmq_delayed_message_exchange-20171201-3.7.x.ez plugins/ && \
    rabbitmq-plugins enable rabbitmq_delayed_message_exchange

# setup healthcheck
HEALTHCHECK --interval=1s --retries=30 CMD ["docker-healthcheck"]
