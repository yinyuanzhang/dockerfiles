FROM ubuntu

RUN apt-get update && \
    apt-get install mysql-client cron bzip2 -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /backups

ENV MYSQL_ENV_MYSQL_HOST mysql
ENV BACKUP_TIME 0 3 * * *

COPY docker-entrypoint.sh /entrypoint.sh
COPY backup restore /bin/

RUN chmod +x /entrypoint.sh
RUN chmod +x /bin/backup
RUN chmod +x /bin/restore

VOLUME /backups

ENTRYPOINT ["/entrypoint.sh"]

CMD ["cron", "-f"]
