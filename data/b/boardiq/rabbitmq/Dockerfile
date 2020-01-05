FROM rabbitmq:management
MAINTAINER Fredrik Eckardt <fredrik.eckardt@boardintelligence.com>

RUN mkdir -p /usr/lib/rabbitmq/plugins
COPY rabbitmq_message_timestamp-20170830-3.7.x.ez /usr/lib/rabbitmq/plugins/

RUN rabbitmq-plugins enable --offline rabbitmq_shovel rabbitmq_shovel_management rabbitmq_message_timestamp
