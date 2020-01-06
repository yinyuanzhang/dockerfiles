FROM alpine:latest

#ENV CONFIG_JSON=none VER=3.36
ENV CONFIG_JSON=none VER=4.6.0

RUN mkdir -m 777 /v2ray

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh 
ENTRYPOINT  /entrypoint.sh 

EXPOSE 8080
