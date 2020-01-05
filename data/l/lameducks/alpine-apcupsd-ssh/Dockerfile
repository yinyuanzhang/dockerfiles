FROM alpine
RUN apk add --no-cache apcupsd openssh-client
COPY apcupsd.conf doshutdown /etc/apcupsd/

VOLUME ["/root/.ssh"]

CMD ["apcupsd", "-b"]
