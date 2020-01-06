FROM ubuntu:bionic

MAINTAINER Sebastian Sterk https://wiuwiu.de/Imprint

COPY run.sh /srv/
COPY housekeeping.sh /srv/

RUN apt-get -y update \
	&& apt-get -y upgrade \
	&& DEBIAN_FRONTEND=noninteractive apt-get -y install apt-utils \ 
	vim \
	telnet \
	netcat \
	mercurial \
	gnupg2 \
        lsb-base \
	lsb-release \
	adduser \
	openssl \
	libssl1.0.0 \
        ca-certificates \
	ssl-cert \
	wget \
	mysql-client \
	&& echo deb http://packages.prosody.im/debian $(lsb_release -sc) main | tee -a /etc/apt/sources.list \
	&& wget https://prosody.im/files/prosody-debian-packages.key -O- | apt-key add - \
	&& apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get -y install prosody \
	lua5.2 \
	lua-event \
	lua-bitop \
        lua-dbi-mysql \
	lua-dbi-postgresql \
	lua-dbi-sqlite3 \
        lua-expat \
        lua-filesystem \
        lua-sec \
        lua-socket \
        lua-zlib \
	busybox-static \
	&& sed -i '1s/^/daemonize = false;\n/' /etc/prosody/prosody.cfg.lua \
	&& mkdir -p /var/run/prosody && chown prosody:adm /var/run/prosody \
	&& mkdir -p /usr/lib/prosody/modules-community \
	&& mkdir -p /var/spool/cron/crontabs \
    	&& echo '* */6 * * * bash /srv/housekeeping.sh' > /var/spool/cron/crontabs/prosody \
	&& chown -R prosody: /usr/lib/prosody/modules-community \
	&& chown -R prosody: /var/lib/prosody \
	&& chown -R prosody: /etc/prosody \
	&& chmod u+x /srv/*.sh \
	&& chown prosody /srv/*.sh \
	&& rm -rf /var/lib/apt/lists/*

COPY http.lua /tmp/
RUN mv /tmp/http.lua /usr/lib/prosody/net/

EXPOSE 80 443 5222 5269 5347 5280 5281 5582 5583

VOLUME ["/etc/prosody", "/var/lib/prosody", "/var/log/prosody", "/usr/lib/prosody/modules-community"]
USER prosody

ENTRYPOINT ["/srv/run.sh"]
CMD ["prosody"]
