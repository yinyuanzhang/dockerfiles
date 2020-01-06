FROM	ubuntu:trusty
MAINTAINER	kload "kload@kload.fr"

RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive \
	echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d && \
	chmod +x /usr/sbin/policy-rc.d && \
	apt-get update && \
	apt-get install -y -q postgresql-9.3 postgresql-contrib-9.3 && \
	apt-get install -y -q postgis postgresql-9.3-postgis-2.1 && \
	rm -rf /var/lib/apt/lists/* && \
	apt-get clean && \
	rm /usr/sbin/policy-rc.d && \
	echo 'host all all 0.0.0.0/0 md5' >> /etc/postgresql/9.3/main/pg_hba.conf && \
	sed -i -e"s/var\/lib/opt/g" /etc/postgresql/9.3/main/postgresql.conf

ADD	. /usr/bin
RUN	chmod +x /usr/bin/start_pgsql.sh
