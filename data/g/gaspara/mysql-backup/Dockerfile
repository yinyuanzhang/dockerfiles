FROM debian:jessie

MAINTAINER Joeri Verdeyen <joeriv@yappa.be>

RUN apt-get update -q && \
    apt-get install -qy cron mysql-client rsync ssh curl && \
    apt-get clean -q

COPY backup.sh run.sh /

ENV CRON_TIME="0 1,9,17 * * *" DBS="" MYSQL_PASSWORD="root" MYSQL_USERNAME="root" MYSQL_HOST="mysql"
ENV NOTIFICATION_SERVICE=""
ENV SLACK_HOOK_URL="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
ENV SLACK_CHANNEL="#monit"
ENV SLACK_USERNAME="container-mysql-backup"
ENV SLACK_EMOJI="package"
ENV RSYNC_COMMAND="rsync -avz -e \"ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null\" %DIR% user@remote:/"
ENV TS_FORMAT="%Y_%m_%d_%H_%M"

CMD ["/run.sh"]
