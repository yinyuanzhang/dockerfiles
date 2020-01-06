FROM rabbitmq:management-alpine

RUN rabbitmq-plugins enable --offline rabbitmq_amqp1_0 && \
    rabbitmq-plugins enable --offline rabbitmq_mqtt && \
    rabbitmq-plugins enable --offline rabbitmq_stomp && \
    rabbitmq-plugins enable --offline rabbitmq_web_stomp

EXPOSE 4369 5671 5672 25672 1883 8883 15672 15674 61613 61614
