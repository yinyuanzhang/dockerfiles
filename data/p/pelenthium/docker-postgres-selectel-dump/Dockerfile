FROM postgres:10-alpine
MAINTAINER Sergey Lugovoy <pelenthium@gmail.com>

VOLUME ["/var/backups"]

ENV BACKUP_DIR /var/backups


RUN apk add curl && \
	rm /var/cache/apk/* && \
	wget https://raw.github.com/selectel/supload/master/supload.sh && \
	mv supload.sh /usr/local/bin/supload && \
	chmod +x /usr/local/bin/supload

ADD sbackup.sh /usr/local/bin/sbackup
ADD entrypoint.sh  /usr/local/bin


ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD crond -f -d 8 -L /var/log/cron.log
