FROM ubuntu:14.04

## Install tools
RUN apt-get update && \
    apt-get install supervisor -y 

## Install Percona
# set apt repository
ENV PERCONA_VERSION 5.6
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A && \
	echo 'deb http://repo.percona.com/apt trusty main' > /etc/apt/sources.list.d/percona.list && \
	apt-get update
# install
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install percona-server-server-$PERCONA_VERSION

## Configure Percona
RUN sed -i -e 's/^bind-address/#bind-address/' /etc/mysql/my.cnf

## Supervisor configuration
ADD config/supervisor-percona.conf /etc/supervisor/conf.d/percona.conf
ADD init.sh /init.sh
RUN chmod +x /init.sh

## Docker config
EXPOSE 3306
CMD ["/init.sh"]
