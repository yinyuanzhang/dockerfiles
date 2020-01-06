#MariaDB (https://mariadb.org/)

FROM phusion/baseimage:0.9.15
MAINTAINER Joshua Lee <muzili@gmail.com>

# Create a directory for the source code.
RUN mkdir -p /var/log/mysql && \
    mkdir -p /data

# Disable SSH (Not using it at the moment).
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Install MariaDB from repository.
ENV MARIADB_MAJOR 10.0
RUN echo "deb http://ftp.osuosl.org/pub/mariadb/repo/$MARIADB_MAJOR/ubuntu trusty main" > /etc/apt/sources.list.d/mariadb.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes mariadb-server mariadb-server-$MARIADB_MAJOR pwgen inotify-tools && \
    locale-gen en_US.UTF-8 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 3306
ADD https://raw.githubusercontent.com/phacility/phabricator/master/resources/sql/stopwords.txt /etc/mysql/stopwords.txt
ADD conf.d/ /etc/mysql/conf.d/
ADD scripts /scripts
RUN chmod +x /scripts/start.sh && \
    chmod 644 /etc/mysql/stopwords.txt && \
    chmod 644 /etc/mysql/conf.d/*.cnf && \
    touch /firstrun

# Expose our data, log, and configuration directories.
VOLUME ["/data", "/var/log/mysql"]

#Added to avoid in container connection to the database with mysql client error message "TERM environment variable not set"
ENV TERM dumb

CMD ["/scripts/start.sh"]
