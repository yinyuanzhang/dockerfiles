# Forked from https://github.com/Kloadut/dokku-pg-dockerfiles

FROM ubuntu:trusty
MAINTAINER Brian Pattison "brian@brianpattison.com"

# Prevent apt from starting postgres right after the installation
RUN	echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d; chmod +x /usr/sbin/policy-rc.d

# Make Postgres 9.4 available for apt-get
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main 9.4" > "/etc/apt/sources.list.d/pgdg.list"
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

RUN apt-get update
RUN	LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y -q postgresql-9.4 postgresql-contrib-9.4 postgresql-client-9.4
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get clean

# Allow autostart again
RUN	rm /usr/sbin/policy-rc.d

ADD	. /usr/bin
RUN	chmod +x /usr/bin/start_pgsql.sh
RUN echo 'host all all 172.17.42.1/16 md5' >> /etc/postgresql/9.4/main/pg_hba.conf
RUN sed -i -e"s/var\/lib/opt/g" /etc/postgresql/9.4/main/postgresql.conf
