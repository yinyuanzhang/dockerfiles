FROM alpine:latest

ENV UUID=none VER=none

RUN mkdir -m 777 /v2raybin
ADD entrypoint.sh /v2raybin/entrypoint.sh
ADD config.json /v2raybin/config.json
RUN chmod +x /v2raybin/entrypoint.sh
ENTRYPOINT  /v2raybin/entrypoint.sh

EXPOSE 8080
