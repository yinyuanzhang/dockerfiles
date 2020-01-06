FROM ubuntu:cosmic
RUN apt-get update && \
    apt-get install -y postfix postfix-mysql syslog-ng

ENV MAIL_DOMAIN    "hoi.fotozupple.de"
ENV ALIAS_DOMAINS  "virtual.hoi.fotozupple.de"
ENV MYSQL_HOST     "mysql"
ENV MYSQL_USER     "mail"
ENV MYSQL_PASSWORD "secret"
ENV MYSQL_DATABASE "mail"
ENV MYSQL_QUERY    "SELECT forw_addr FROM aliases WHERE alias='%s'"

RUN echo "localhost" > /etc/mailname
COPY main.cf /etc/postfix/main.cf
COPY generic /etc/postfix/generic
COPY docker-entry.sh /usr/bin/postfix-docker-entry

EXPOSE 25
ENTRYPOINT ["/usr/bin/postfix-docker-entry"]
