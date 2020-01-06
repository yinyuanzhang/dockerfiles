FROM rabbitmq:3-management

RUN rabbitmq-plugins enable --offline rabbitmq_shovel_management
RUN rabbitmq-plugins enable --offline rabbitmq_web_stomp

EXPOSE 15673 15674