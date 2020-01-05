## MySQL 5.6 with Xtrabackup
FROM mysql:5.6

LABEL maintainer="John Hoker"
LABEL version="1.0"

ENV PACKAGE percona-xtrabackup-22
ENV MYSQL_ROOT_PASSWORD=hoker11

## Install requirement (wget)
RUN apt-get update && \
    apt-get install -y wget && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8507EFA5
 

## Install Xtrabackup
RUN wget https://repo.percona.com/apt/percona-release_0.1-3.jessie_all.deb && \
    dpkg -i percona-release_0.1-3.jessie_all.deb && \
    apt-get update && \
    apt-cache search percona-xtrabackup && \
    apt-get install -y ${PACKAGE}

## Create the backup destination
RUN mkdir -p /backup/xtrabackup

ADD run_backup.sh /run_backup.sh

## Allow moutable backup path
VOLUME [ "/backup/xtrabackup" ]
