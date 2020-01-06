FROM certbot/certbot:latest

RUN apk update && apk upgrade && apk add rabbitmq-c-utils bash jq

ADD ./rabbit.sh /rabbit.sh
RUN chmod a+x /rabbit.sh
ADD ./entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
