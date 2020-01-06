FROM alpine:3.3

RUN apk add --update nodejs git && mkdir /app

ADD ./config/start.sh /home/

RUN chmod u+x /home/start.sh

CMD ["/home/start.sh"]
