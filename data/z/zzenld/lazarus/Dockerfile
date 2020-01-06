FROM alpine:latest
MAINTAINER ZzenlD

RUN apk add --no-cache bash samba pwgen && \
    mkdir data var/cache/lazarus && \
    echo '0 1 * * * bash /lazarus.sh' > /var/spool/cron/crontabs/root && \
    chmod 0777 data

COPY smb.conf /etc/samba/smb.conf
COPY lazarus.sh /lazarus.sh

EXPOSE 445/tcp

ENV DAYS_BEFORE_WARNING=30 \
    DAYS_BEFORE_ALERT=60

CMD echo "********* Starting Lazarus *********" && crond -f
