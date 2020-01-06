FROM alpine:edge
ARG DOVECOT_VERSION=2.3.3-r0
RUN apk add --no-cache dovecot dovecot-lmtpd dovecot-pop3d ca-certificates && mkdir /var/vpopmail && chown 89:89 /var/vpopmail
COPY 91-docker.conf /etc/dovecot/conf.d/91-docker.conf
EXPOSE 143 993 110 995 26
ENTRYPOINT ["dovecot", "-F"]
