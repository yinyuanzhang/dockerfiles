FROM centos:7

LABEL maintainer="Florian Probst <flo@nodi.at>"

VOLUME /data

USER root

RUN yum -y update && yum clean all
RUN \
        yum install epel-release -y && \
        yum groupinstall -y development && \
        yum install -y \
		GraphicsMagick \
		GraphicsMagick-c++ \
		GraphicsMagick-c++-devel \
		GraphicsMagick-devel \
		boost-python \
		boost-python-devel \
		bzip2-devel \
		gifsicle \
		jasper-devel \
		libcurl-devel \
		libdc1394 \
		libffi \
		libffi-devel \
		libjpeg-turbo \
		libjpeg-turbo-devel \
		libjpeg-turbo-utils \
		libmemcached-devel \
		libpng-devel \
		libtiff-devel \
		libwebp-devel \
		opencv-devel \
		opencv-python \
		openssh-devel \
		openssl \
		openssl-devel \
		pngcrush \
		pycurl \
		python-cffi \
		python-devel \
		python-pip \
		python-pillow \
		python-pillow-devel \
		python-setuptools \
		sqlite-devel \
		sudo \
		tar \
		zlib-devel && \
	yum clean all

ENV HOME /app
ENV SHELL bash
ENV WORKON_HOME /app

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir \
	-r /app/requirements.txt

COPY conf/thumbor.conf.tpl /app/thumbor.conf.tpl

RUN adduser -d /app thumbor && \
	chown -R thumbor: /app && \
	chown -R thumbor: /data

USER thumbor

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

HEALTHCHECK --start-period=30s --retries=3 --interval=30s --timeout=10s \ 
	CMD curl -f http://127.0.0.1:8080/healthcheck

EXPOSE 8080 8888
