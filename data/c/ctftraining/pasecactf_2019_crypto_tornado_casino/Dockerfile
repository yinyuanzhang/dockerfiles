FROM python:3.7-alpine

RUN apk add --no-cache socat
COPY ./files /service
EXPOSE 1337
CMD sh /service/deploy.sh

