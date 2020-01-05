FROM prima/php:7.2.24-4

RUN apt-get update && apt-get install -y cron && \
    rm -r /var/lib/apt/lists/* && \
    apt-get update && apt-get install -y python python-pip unzip redis-tools rsync && \
    pip install --upgrade awscli && \
    aws configure set s3.signature_version s3v4 && \
    apt-get purge -y python-pip && \
    rm -r /var/lib/apt/lists/* && \
    mkdir -p /etc/cron.d && \
    mkdir -p /var/log/prima && \
    php -v

COPY crontab/documents_importer /documents_importer
COPY crontab/heartbeat /heartbeat
COPY files/run-as-cron.sh /root/run-as-cron.sh
COPY files/cronrc /root/cronrc
COPY files/entrypoint.sh /entrypoint.sh

RUN chmod +x /root/run-as-cron.sh && \
    chmod +x /root/cronrc && \
    chmod +x /entrypoint.sh
