FROM rabbitmq:3.7

LABEL maintainer="Herson Melo <hersonpc@gmail.com>"

USER root

RUN rabbitmq-plugins enable --offline rabbitmq_management
RUN rabbitmq-plugins enable --offline rabbitmq_stomp
RUN rabbitmq-plugins enable --offline rabbitmq_web_stomp

ADD ./init.sh /app/init.sh
RUN chmod +x /app/init.sh

WORKDIR /app

EXPOSE 5672 15671 15672 15674 61613

CMD [ "/app/init.sh" ]