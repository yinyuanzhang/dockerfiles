FROM nishidayuya/centos-buildpack-deps:centos7-scm

# Following codes are modified from:
# https://github.com/docker-library/buildpack-deps/blob/b0fc01aa5e3aed6820d8fed6f3301e0542fbeb36/stretch/Dockerfile

RUN set -ex; \
	yum update -y; \
	yum install -y \
		autoconf \
		automake \
		bzip2 \
		file \
		gcc-c++ \
		gcc \
		ImageMagick \
		bzip2-devel \
		glibc-devel \
		libcurl-devel \
		libdb-devel \
		libevent-devel \
		libffi-devel \
		gdbm-devel \
		GeoIP-devel \
		glib2-devel \
		libjpeg-turbo-devel \
		krb5-devel \
		xz-devel \
		ImageMagick-devel \
		ncurses-devel \
		libpng-devel \
		postgresql-devel \
		readline-devel \
		sqlite-devel \
		openssl-devel \
		libtool \
		libwebp-devel \
		libxml2-devel \
		libxslt-devel \
		libyaml-devel \
		make \
		patch \
		xz \
		zlib-devel \
		\
		mariadb-devel \
	; \
	rm -rf /var/cache/yum/*
