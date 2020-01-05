FROM alpine:3.8

RUN apk --no-cache add monit=5.25.1-r1

VOLUME /etc/monit.d/

EXPOSE 2812

CMD ["monit", "-I", "-B"]