FROM alpine:3.10
LABEL maintainer="jeff@reverentengineer.com"
ENV TLS_CERT /etc/ssl/dovecot/server.pem
ENV TLS_KEY /etc/ssl/dovecot/server.key
ENV LDAP_HOST openldap
ENV LDAP_BIND_TEMPLATE "cn=%u,ou=people,dc=example,dc=org"
RUN apk update && \
  apk add --no-cache dovecot dovecot-ldap dovecot-lmtpd && \
  mkdir -p /var/lib/mail && \
  addgroup -S vmail &&\
  adduser -h /var/lib/mail -S -G vmail vmail
ADD ./dhparams.pem /etc/dovecot/
ADD ./dovecot.conf /etc/dovecot/
ADD ./docker-entrypoint.sh .
VOLUME /var/lib/mail
EXPOSE 24 143 993 12345
CMD ["./docker-entrypoint.sh"]
