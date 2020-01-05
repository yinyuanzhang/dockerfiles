FROM onesysadmin/ubuntu-postfix

RUN apt-get -y update
RUN apt-get -y install rsyslog
RUN update-rc.d rsyslog defaults 90

COPY ./scripts/postfix-start.sh /app/postfix-start.sh
RUN chmod +x /app/postfix-start.sh

EXPOSE 25

ENTRYPOINT ["/app/postfix-start.sh"]