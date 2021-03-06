# A Docker BUILDER image with
# XTA (XA Transaction API) for Java language
# based on official Maven image
FROM	openjdk:jdk-slim AS builder
#
# Build without parameters to build latest
#	docker build -f Dockerfile-jdk-maven -t lixa/xta-jdk-maven .
# Build with 2 parameters to build a specific release
#	docker build --build-arg VERSION_CODE=1.7.8 \
#		--build-arg VERSION_TYPE=testing -t lixa/xta-jdk-maven:1.7.8 .
#   ** Note: version code must be of the right type and must exists in
#            Sourceforge.net
# Build with specific configure options as for example
#       docker build -f Dockerfile-jdk-maven \
#               --build-arg CONFIG_OPTIONS="--enable-crash" \
#               -t lixa/xta-jdk-maven .
# Inspect the image content with
#	docker run --rm -it lixa/xta-jdk-maven bash
#
# Update Debian Software repository
ARG 	DEBIAN_FRONTEND=noninteractive
# Install generic pre-requisites
RUN	apt-get update && apt-get install -y --no-install-recommends \
	apt-utils \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf /var/log/* 
# Additional specific configuration options
ARG	CONFIG_OPTIONS
ENV	CONFIG_OPTIONS $CONFIG_OPTIONS
# LIXA official package
# VERSION_CODE must be in format V.R.M and it must be available on Sourceforge
# VERSION_TYPE must be "stable" or "testing"
# elsewhere, latest will be used
ARG	VERSION_CODE
ARG	VERSION_TYPE
ENV	VERSION_CODE $VERSION_CODE
ENV	VERSION_TYPE $VERSION_TYPE
ENV	LIXA_VERSION $VERSION
ENV	LIXA_DOWNLOAD_DEF_URL https://sourceforge.net/projects/lixa/files/latest/download
ENV	LIXA_DOWNLOAD_VER_URL https://sourceforge.net/projects/lixa/files/lixa/$VERSION_TYPE/lixa-$VERSION_CODE.tar.gz/download
ENV	POSTGRESQL_JDBC_URL https://jdbc.postgresql.org/download/postgresql-42.2.5.jar
# build LIXA
RUN	BUILD_DEPS='ca-certificates wget make gcc pkg-config libxml2-dev libglib2.0-dev uuid-dev libpq-dev default-libmysqlclient-dev libmysql-java' \
	&& set -x \
	&& apt-get update && apt-get install -y --no-install-recommends \
		$BUILD_DEPS
RUN	mkdir -p /lixa \
	&& if [ "z$VERSION_CODE" != "z" -a "z$VERSION_TYPE" != "z" ]; \
		then wget -O lixa.tar.gz "$LIXA_DOWNLOAD_VER_URL"; \
		else wget -O lixa.tar.gz "$LIXA_DOWNLOAD_DEF_URL"; \
	   fi \
	&& tar -xzf lixa.tar.gz -C /lixa \
	&& rm lixa.tar.gz
RUN	mkdir -p /opt/postgresql \
	&& wget -O /opt/postgresql/postgresql.jar "$POSTGRESQL_JDBC_URL"
RUN	cd /lixa/lixa-* \
	&& ./configure --disable-syslog --disable-server \
		--disable-xta-cpp --disable-xta-python \
		--with-mysql-jdbc=/usr/share/java/mysql.jar \
		--with-postgresql-jdbc=/opt/postgresql/postgresql.jar \
		$CONFIG_OPTIONS \
	&& make && make install
RUN	rm -rf /opt/lixa/share/doc /opt/lixa/include \
		/opt/lixa/bin/lixatpm /opt/lixa/bin/lixavsr \
	&& rm -r /lixa \
	&& apt-get purge -y --auto-remove $BUILD_DEPS \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf /var/log/* /opt/lixa/var \
	&& mv -v /opt/lixa/etc/lixac1_conf.xml /opt/lixa/etc/lixac_conf.xml \
	&& rm /opt/lixa/etc/lixad*_conf.xml

# A Docker run-time image with
# XTA (XA Transaction API) for Java language
# based on official Maven image
FROM	maven:slim
# Update Debian Software repository
ARG 	DEBIAN_FRONTEND=noninteractive
# Install generic pre-requisites
RUN	apt-get update && apt-get install -y --no-install-recommends \
	apt-utils \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf /var/log/* 
# Install run-time pre-requisites
RUN	apt-get update && apt-get install -y --no-install-recommends \
	libxml2 libglib2.0 uuid-runtime \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf /var/log/* \
	&& mkdir -p /opt/lixa/bin /opt/lixa/etc /opt/lixa/lib/ \
		/opt/java
COPY	--from=builder /opt/lixa/bin/* /opt/lixa/bin/
COPY	--from=builder /opt/lixa/etc/* /opt/lixa/etc/
COPY	--from=builder /opt/lixa/lib/* /opt/lixa/lib/
COPY	--from=builder /opt/lixa/lib/* /opt/lixa/lib/
COPY	--from=builder /opt/lixa/share/lixa/java/* /opt/java/
COPY    --from=builder /opt/postgresql/postgresql.jar /opt/java/
