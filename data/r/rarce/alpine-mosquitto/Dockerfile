FROM alpine:3.4

RUN apk add --no-cache \
    mosquitto \
    mosquitto-clients

EXPOSE 1883
ENTRYPOINT ["mosquitto"]
