FROM ubuntu:latest

# ENV AWS_ACCESS_KEY_ID
# ENV AWS_SECRET_ACCESS_KEY
ENV AWS_DEFAULT_REGION=ap-southeast-1
# ENV S3_BUCKET
ENV MYSQL_HOST=main-mysql
ENV MYSQL_USER=xtradbbackup
# ENV MYSQL_PASSWORD
ENV MYSQL_PORT=3306

RUN touch /var/log/cron.log && mkdir /backups && mkdir /etc/cron.d

RUN apt-get update && apt-get install curl wget lsb-release unzip python cron -y && \
    curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" && \
    unzip awscli-bundle.zip && \
    ./awscli-bundle/install -b /root/aws
    
RUN wget https://repo.percona.com/apt/percona-release_0.1-4.$(lsb_release -sc)_all.deb && \
    dpkg -i percona-release_0.1-4.$(lsb_release -sc)_all.deb && \
    apt-get update && \
    apt-get install percona-xtrabackup-24 -y

RUN echo "0 3 * * * bash /root/backup.sh auto >> /var/log/cron.log 2>&1" >> /etc/cron.d/backup
RUN chmod 0644 /etc/cron.d/backup

ADD backup.sh /root/backup.sh

CMD cron && tail -f /var/log/cron.log
