FROM rabbitmq:3-management-alpine

MAINTAINER <vk@alphacloud.net>

RUN rabbitmq-plugins enable --offline rabbitmq_shovel rabbitmq_shovel_management

ENV RABBITMQ_SERVER_CODE_PATH=/tmp/rabbit-hipe/ebin

RUN rabbitmqctl hipe_compile /tmp/rabbit-hipe/ebin
