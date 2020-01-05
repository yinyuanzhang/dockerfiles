FROM ubuntu:16.04

## Ask nothing when install with apt or deb
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y software-properties-common language-pack-en-base \
    && apt-get update \
    && apt-get install -y -f gearman-tools gearman-job-server mysql-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

## Expose the standard port for gearman
EXPOSE 4730

# set some defaults

ENV MYSQL_ROOT_PASSWORD pass
ENV MYSQL_DATABASE gearman
ENV MYSQL_USER gearman
ENV MYSQL_PASSWORD gearman
ENV MYSQL_PORT 3306
ENV MYSQL_HOST 127.0.0.1



COPY ./run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]



