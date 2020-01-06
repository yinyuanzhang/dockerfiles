FROM ubuntu:trusty
MAINTAINER Jonathan Tse <jtse@proactivesystem.com.hk>

RUN apt-get update && \
    apt-get install -y --no-install-recommends mysql-client && \
    mkdir /backup

ENV CRON_TIME="0 0 * * *" \
    MYSQL_DB="--all-databases"
ADD run.sh /run.sh
VOLUME ["/backup"]

CMD ["/run.sh"]
