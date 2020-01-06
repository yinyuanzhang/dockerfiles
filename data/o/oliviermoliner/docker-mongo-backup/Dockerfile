FROM mongo:latest


RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10 \
    && apt-get update \
    && apt-get install -y ca-certificates cron python-pip \
    && pip install awscli \
    && mkdir /backup

ENV CRON_TIME="0 0 * * *"
ENV S3_PATH=mongobackup
ENV AWS_DEFAULT_REGION=eu-west-1

ADD docker_entrypoint.sh /docker_entrypoint.sh
ADD backup.sh /backup.sh

CMD ["/docker_entrypoint.sh"]
