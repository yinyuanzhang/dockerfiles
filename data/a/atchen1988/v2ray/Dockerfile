FROM alpine:latest

# ENV CONFIG_JSON=none CERT_PEM=none KEY_PEM=none VER=4.5.0

RUN mkdir -m 777 /v2ray

ADD entrypoint.sh /entrypoint.sh
ADD config.json /config.json
RUN chmod +x /entrypoint.sh 
ENTRYPOINT  /entrypoint.sh 

EXPOSE 8080