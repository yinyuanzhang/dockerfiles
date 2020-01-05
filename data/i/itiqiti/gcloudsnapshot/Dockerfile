FROM google/cloud-sdk

RUN apt-get update && apt-get install -y cron

COPY snapshot.sh /usr/local/bin/

COPY crontab /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab

CMD ["cron", "-f"]
