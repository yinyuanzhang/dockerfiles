FROM ubuntu:16.04
MAINTAINER Brian Holman <bholman@dezota.com>

ENV DEBIAN_FRONTEND=noninteractive

# Set default timezone
RUN ln -fs /usr/share/zoneinfo/America/Denver /etc/localtime

# Ensure everything is up-to-date
RUN apt-get update --fix-missing && \
    apt-get -y upgrade

# Install System Packages
RUN apt-get install -y wget software-properties-common python-software-properties apt-transport-https sudo locales tzdata git

# Generate Locale
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen 

# Dockerized systemctl and grab MYSQL Community Docker build scripts
RUN wget -O /usr/bin/systemctl "https://raw.githubusercontent.com/gdraheim/docker-systemctl-replacement/master/files/docker/systemctl.py" && \
    wget -O /entrypoint.sh "https://raw.githubusercontent.com/mysql/mysql-docker/mysql-server/8.0/docker-entrypoint.sh" && \
    wget -O /healthcheck.sh "https://raw.githubusercontent.com/mysql/mysql-docker/mysql-server/8.0/healthcheck.sh" && \
    chmod +x /usr/bin/systemctl /entrypoint.sh /healthcheck.sh

# Set policy
RUN echo exit 101 > /usr/sbin/policy-rc.d && \
    chmod +x /usr/sbin/policy-rc.d
    
# Configure MYSQL repo and install MYSQL Server
RUN wget https://dev.mysql.com/get/mysql-apt-config_0.8.10-1_all.deb && \
    dpkg -i mysql-apt-config_0.8.10-1_all.deb && \
    apt-get update && \
    rm /mysql-apt-config_0.8.10-1_all.deb

RUN mkdir /docker-entrypoint-initdb.d
    
RUN apt-get install -yq mysql-server; exit 0

RUN chown mysql:mysql /usr/sbin/mysqld && \
    chmod 4750 /usr/sbin/mysqld && \
    ln -s /etc/mysql/mysql.cnf /etc/my.cnf

ENV MYSQL_ROOT_PASSWORD="Chang3M3R1ghtN0w" TZ="America/Denver"

COPY importdb.sh /docker-entrypoint-initdb.d/importdb.sh
COPY legacypw.cnf /etc/mysql/mysql.conf.d/legacypw.cnf

RUN touch /firstime && \
    chmod +x /docker-entrypoint-initdb.d/importdb.sh && \
    rm -f /usr/share/zoneinfo/iso3166.tab /usr/share/zoneinfo/leap-seconds.list /usr/share/zoneinfo/zone.tab /usr/share/zoneinfo/zone1970.tab

ENTRYPOINT ["/entrypoint.sh"]
HEALTHCHECK CMD /healthcheck.sh
EXPOSE 3306 33060
CMD ["mysqld"]
