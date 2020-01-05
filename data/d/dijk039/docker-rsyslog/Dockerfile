FROM alpine:3.5
MAINTAINER dijk039@gmail.com

RUN  apk add --update rsyslog \
  && rm -rf /var/cache/apk/*

EXPOSE 514 514/udp

VOLUME [ "/var/log", "/etc/rsyslog.d" ]

COPY rsyslog.conf /etc/rsyslog.conf

ENTRYPOINT [ "rsyslogd", "-n" ]
