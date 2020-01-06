FROM alpine

MAINTAINER Helmuth Breitenfellner <helmuth@breitenfellner.at>

VOLUME /backup
VOLUME /data

ENV BACKUP_NAME=localhost
ENV BACKUP_SOURCE=/data
ENV BACKUP_OPTS=one_fs=1
ENV BACKUP_HOURLY=0
ENV BACKUP_DAILY=3
ENV BACKUP_WEEKLY=3
ENV BACKUP_MONTHLY=3
ENV BACKUP_YEARLY=3

RUN touch /ssh-id && touch /backup.cfg

RUN apk add --update rsnapshot tzdata

ADD entry.sh /entry.sh

CMD ["/bin/sh", "/entry.sh"]
