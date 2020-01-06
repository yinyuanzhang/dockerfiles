FROM alpine:latest
MAINTAINER chris@arraylabs.com
 
RUN apk update && apk add dcron wget rsync ca-certificates sshpass openssh-client bash bash-doc bash-completion tar python python-dev py-pip build-base && rm -rf /var/cache/apk/*

RUN pip install pysnmp
RUN pip install requests
RUN pip install workalendar

RUN mkdir -p /var/log/cron && mkdir -m 0644 -p /var/spool/cron/crontabs && touch /var/log/cron/cron.log && mkdir -m 0644 -p /etc/cron.d

COPY /scripts/* /

ENTRYPOINT ["/docker-entry.sh"]
CMD ["/docker-cmd.sh"]
