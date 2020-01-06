FROM centos:latest
ENV VERSION=1.5.3
RUN yum -y update && yum -y install epel-release && \
	yum -y install jq wget nodejs bzip2 curl net-tools fontconfig freetype freetype-devel fontconfig-devel libyaml-devel libpcap-devel libstdc++ ethtool pcre tcpdump pcre-devel libyaml pkgconfig flex bison gcc-c++ zlib-devel e2fsprogs-devel openssl-devel file-devel make gettext libuuid-devel perl-JSON bzip2-libs bzip2-devel perl-libwww-perl libpng-devel xz libffi-devel GeoIP vim && \
	wget https://files.molo.ch/builds/centos-7/moloch-$VERSION-1.x86_64.rpm && \
	rpm -i moloch-$VERSION-1.x86_64.rpm

ADD scripts /data/moloch/

ENV ES_HOST=elasticsearch \
	INTERFACE=eth0 \
	CLUSTER_PW=secretpw \
	ADMIN_PW=supersecretpw \
	SENSOR=true

RUN chmod +x /data/moloch/*.sh && \
	chmod +x /data/moloch/db/db.pl /data/moloch/*/*.sh && \
	cd /data/moloch/viewer && \
	ln -s /data/moloch/bin/node /usr/bin/nodejs && \
	npm update . && \
	npm install . && \
	yum clean -y all

ADD etc/config.ini /data/moloch/etc/config.ini
RUN chmod 755 /data/moloch/etc/config.ini

EXPOSE 8005

WORKDIR /data/moloch

ENTRYPOINT ["./docker-entrypoint.sh"]
