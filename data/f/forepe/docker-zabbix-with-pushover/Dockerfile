FROM rabbitmq:management
MAINTAINER Peter Foreman <peter@frmn.nl>

RUN apt-get update && apt-get -y upgrade
RUN rabbitmq-plugins enable rabbitmq_mqtt rabbitmq_shovel rabbitmq_shovel_management rabbitmq_stomp rabbitmq_top rabbitmq_web_mqtt rabbitmq_web_stomp
