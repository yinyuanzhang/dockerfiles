FROM alpine:3.10

RUN apk add --no-cache dovecot=2.3.7.2-r0 dovecot-pigeonhole-plugin=2.3.7.2-r0 dovecot-lmtpd=2.3.7.2-r0

VOLUME "/etc/dovecot"

EXPOSE 143
EXPOSE 993

ENTRYPOINT ["/usr/sbin/dovecot", "-F"]
