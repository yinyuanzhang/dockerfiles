FROM java:8
MAINTAINER André Camilo <andrejcamilo@gmail.com>

# Download bitbucket backup client

ENV BITBUCKET_BACKUP_CLIENT_VERSION 3.3.4
ENV VERSION_LINK 300300410

RUN curl -Lks https://marketplace.atlassian.com/download/apps/1211500/version/${VERSION_LINK} -o /root/bitbucket-backup-client.zip
RUN mkdir /opt/bitbucket
RUN unzip /root/bitbucket-backup-client.zip -d /opt/bitbucket
RUN mv /opt/bitbucket/bitbucket-backup-client-* /opt/bitbucket/bitbucket-backup-client

ADD run-backup.sh /usr/bin/backup
RUN chmod +x /usr/bin/backup
ADD run-restore.sh /usr/bin/restore
RUN chmod +x /usr/bin/restore

WORKDIR /opt/bitbucket

VOLUME /backups
VOLUME /var/atlassian/application-data/bitbucket

# Environment variables
ENV BACKUP_HOME /backups
ENV BITBUCKET_HOME /var/atlassian/application-data/bitbucket

CMD ["backup"]
