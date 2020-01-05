FROM node:11.8.0-alpine

RUN apk add --update git && mkdir /app

ADD ./config/start.sh /home/

RUN chmod u+x /home/start.sh

CMD ["/home/start.sh"]