FROM debian:stretch-slim

LABEL description="piler container with php"
ENV DEBIAN_FRONTEND=noninteractive


ENV PILER_USER="piler"
ENV PILER_GROUP="piler"

ENV MYSQL_HOSTNAME="localhost"
ENV MYSQL_PORT="3306"
ENV MYSQL_DATABASE="piler"
ENV MYSQL_USERNAME="piler"
ENV MYSQL_PASSWORD="piler123"
ENV MYSQL_ROOT_PASSWORD="abcde123"


ARG VERSION=1.3.4
ARG BUILD_DATE

ARG XLHTML_URL="https://bitbucket.org/jsuto/piler/downloads/xlhtml-0.5.1-sj-mod.tar.gz"
ARG SPHINX_URL="http://sphinxsearch.com/files/sphinx-2.3.2-beta.tar.gz"
ARG PILER_URL="https://bitbucket.org/jsuto/piler/downloads/piler-1.3.4.tar.gz"
#ARG PILER_URL="https://bitbucket.org/jsuto/piler/get/master.tar.gz"
ARG DOCROOT=/var/piler/www



WORKDIR /usr/src

RUN groupadd ${PILER_GROUP} ; useradd -g ${PILER_GROUP} -m -s /bin/sh -d /var/piler ${PILER_USER} ; \
    usermod -L ${PILER_USER} ; chmod 755 /var/piler ; \
    \
    fetchDeps=" \
	ca-certificates \
	dirmngr \
	gnupg \
	wget \
        wget curl rsyslog sysstat net-tools mc \
    "; \
    apt-get update; \
    apt-get install -y --no-install-recommends $fetchDeps; \
    rm -rf /var/lib/apt/lists/*; \
    \
    \
    echo "fetching $XLHTML_URL ..." ; \
    wget -O xlhtml.tar.gz "$XLHTML_URL" ; \
    if test ! -f "xlhtml.tar.gz" ; then exit 1; fi; \
    echo "fetching $SPHINX_URL ..." ; \
    wget -O sphinx.tar.gz "$SPHINX_URL" ; \
    if test ! -f "sphinx.tar.gz" ; then exit 1; fi; \
    echo "fetching $PILER_URL ..." ; \
    wget -O piler.tar.gz "$PILER_URL"; \
    if test ! -f "piler.tar.gz" ; then exit 1; fi; \
    \
    buildBasics=' \
	ca-certificates \
	wget apt-utils \
	\
	gcc \
	libc6-dev \
	make \
        build-essential autoconf automake autotools-dev \
    '; \
    \
    buildDeps=' \
	libmariadb-dev \
        libmariadbclient-dev \
        libssl-dev libtre-dev \
        libwrap0-dev \
        libmemcached-dev \
    '; \
    \
    runDeps=' \
	cron sudo procps tzdata rsyslog openssl netcat-traditional \
        fetchmail \
        catdoc unrtf poppler-utils \
        tnef libodbc1 libpq5 libzip4 \
        libtre5 libwrap0 \
        mariadb-client libmariadbclient18 python python-mysqldb libpst4 \
    '; \
    apt-get update; \
    apt-get install -y $buildBasics $buildDeps $runDeps --no-install-recommends; \
    \
    \
    apt-get install -y --no-install-recommends \
    coreutils php7.0-fpm php7.0-cli php7.0-cgi php7.0-mysql php7.0-zip php7.0-ldap php7.0-gd php7.0-curl php7.0-xml ;\
    rm -rf /var/lib/apt/lists/*; \
    \
    mkdir /run/php \
    && { \
	echo '[global]'; \
	echo 'error_log = /proc/self/fd/2'; \
	echo; \
	echo '[www]'; \
	echo '; if we send this to /proc/self/fd/1, it never appears'; \
	echo 'access.log = /proc/self/fd/2'; \
	echo; \
	echo 'clear_env = no'; \
	echo; \
	echo '; Ensure worker stdout and stderr are sent to the main error log.'; \
	echo 'catch_workers_output = yes'; \
    } | tee /etc/php/7.0/fpm/pool.d/docker.conf \
    && { \
	echo '[global]'; \
	echo 'daemonize = no'; \
	echo; \
	echo '[www]'; \
	echo 'listen = 9000'; \
    } | tee /etc/php/7.0/fpm/pool.d/zz-docker.conf && \
    \
    \
    mkdir -p /usr/src/xlhtml-sj-mod; \
    tar -xzf xlhtml.tar.gz -C /usr/src/xlhtml-sj-mod --strip-components=1; \
    rm xlhtml.tar.gz; \
    cd /usr/src/xlhtml-sj-mod && ./configure && make && make install; \
    cd /usr/src ; \
    rm -r /usr/src/xlhtml-sj-mod; \
    \
    \
    mkdir -p /usr/src/sphinx; \
    tar -xzf sphinx.tar.gz -C /usr/src/sphinx --strip-components=1; \
    rm sphinx.tar.gz; \
    cd /usr/src/sphinx && ./configure --prefix=/usr  && make && make install; \
    cd /usr/src ; \
    rm -r /usr/src/sphinx; \
    \
    \
    mkdir -p /usr/src/piler; \
    tar -xzf piler.tar.gz -C /usr/src/piler --strip-components=1; \
    rm piler.tar.gz; \
    cd /usr/src/piler && ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --with-database=mysql --enable-tcpwrappers --enable-memcached && \
    make && make install && \
    mkdir -p "$DOCROOT" && \
    cp -R webui/* "$DOCROOT" && \
    cp webui/.htaccess "$DOCROOT" && \
    chmod 770 "${DOCROOT}/tmp" "${DOCROOT}/images" && \
    chown "$PILER_USER" "${DOCROOT}/tmp" && \
    chgrp "www-data" "${DOCROOT}/tmp" && \
    cd /usr/src ; \
    apt-get purge -y --auto-remove $buildBasics $buildDeps; 



ADD files/piler-nginx.conf /etc/piler/piler-nginx.conf
ADD files/piler.cron /tmp/piler.cron
ADD files/config-site.php /etc/piler/config-site.php
ADD files/fetchmailrc.dist /etc/piler/fetchmailrc.dist
ADD files/services /etc/services
ADD files/piler_backup.sh /etc/cron.daily/piler_backup.sh
ADD files/wait-for /usr/bin/wait-for
ADD start.sh /usr/local/bin/start.sh


RUN \
    sed -i 's/mail.[iwe].*//' /etc/rsyslog.conf && \
    sed -i '/session    required     pam_loginuid.so/c\#session    required     pam_loginuid.so' /etc/pam.d/cron && \
    printf "[mysql]\nuser = ${MYSQL_USERNAME}\npassword = ${MYSQL_PASSWORD}\n" > /etc/piler/.my.cnf && \
    echo "alias mysql='mysql --defaults-file=/etc/piler/.my.cnf'" > /root/.bashrc && \
    echo "alias t='tail -f /var/log/syslog'" >> /root/.bashrc && \
    rm -f /etc/localtime && \
    ln -s  /usr/share/zoneinfo/Europe/Berlin /etc/localtime ; \
    \
    \
    echo "\nSTART_DAEMON=yes" >> /etc/default/fetchmail && \
    crontab -u $PILER_USER /tmp/piler.cron && \
    rm -f $CRON_TMP && \
    touch /var/log/mail.log && \
    sed -i 's/#ngram/ngram/g' /etc/piler/sphinx.conf.dist && \
    sed -i 's/127.0.0.1://g' /etc/piler/sphinx.conf.dist && \
    sed -i "/sql_pass =/ a    sql_port = ${MYSQL_PORT}" /etc/piler/sphinx.conf.dist && \
    cp -a /var/piler /var/piler.sik; \
    cp -a /etc/piler /etc/piler.sik



VOLUME ["/var/piler", "/etc/piler"]

#EXPOSE 25 = smtp, 9306 = sphinx, 9000 = php
EXPOSE 25/tcp 9306/tcp 9000

ADD start.sh /usr/local/bin/start.sh
CMD ["/usr/local/bin/start.sh"]
