FROM debian:jessie

ENV GOSU_VERSION=1.9

RUN apt-get update \
	&& apt-get install -y --no-install-recommends ca-certificates wget \
	&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
	&& wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
	&& wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
	&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu \
	&& gosu nobody true \
	&& rm -rf /var/lib/apt/lists/*

RUN bash -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >> /etc/apt/sources.list.d/pgdg.list' \
	&& (wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -) \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends \
		nano \
		cron \
		gcc \
		libpq-dev \
		libpython-dev \
		logrotate \
		openssh-client \
		postgresql-client-9.4 \
		postgresql-client-9.5 \
		postgresql-client-9.6 \
		postgresql-client-11 \
		python \
		rsync \
		&& rm -rf /var/lib/apt/lists/* 

# Set up some defaults for file/directory locations used in entrypoint.sh.
ENV \
	BARMAN_VERSION=2.5 \
	BARMAN_DATA_DIR=/var/lib/barman \
	BARMAN_LOG_DIR=/var/log/barman 
VOLUME /var/log/barman

COPY install_barman.sh /tmp/
RUN /tmp/install_barman.sh && rm /tmp/install_barman.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["cron", "-L", "0",  "-f"]
COPY entrypoint.sh /
COPY update_secure_files /usr/bin/
WORKDIR ${BARMAN_DATA_DIR}