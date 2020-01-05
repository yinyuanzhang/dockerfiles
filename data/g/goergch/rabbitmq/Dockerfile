FROM rabbitmq:3-management
#web-mqtt
EXPOSE 15675
#management
EXPOSE 15672
#mqtt
EXPOSE 1883

RUN rabbitmq-plugins enable --offline rabbitmq_mqtt rabbitmq_federation rabbitmq_federation_management rabbitmq_web_mqtt rabbitmq_shovel rabbitmq_shovel_management
