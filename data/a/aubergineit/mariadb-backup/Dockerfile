FROM mariadb:10.2

ENV MARIABACKUP_HOST localhost
ENV MARIABACKUP_DATADIR /var/lib/mysql
ENV MARIABACKUP_BACKUPDIR /backups

COPY ./job-backup.sh /usr/local/bin/job-backup.sh
COPY ./job-restore.sh /usr/local/bin/job-restore.sh

RUN chmod a+x /usr/local/bin/job-backup.sh && chmod a+x /usr/local/bin/job-restore.sh

CMD [ "/usr/local/bin/job-backup.sh" ]
