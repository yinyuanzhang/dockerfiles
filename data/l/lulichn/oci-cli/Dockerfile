FROM python:3.7-alpine

MAINTAINER lulichn

ENV VERSION 2.5.18

RUN set -ex \
	&& apk add --no-cache --virtual builddeps build-base libffi-dev openssl-dev \
	&& cd /opt \
	&& wget https://github.com/oracle/oci-cli/releases/download/v${VERSION}/oci-cli-${VERSION}.zip \
	&& unzip oci-cli-${VERSION}.zip \
	&& rm oci-cli-${VERSION}.zip \
	&& cd oci-cli \
	&& pip install oci_cli-${VERSION}-py2.py3-none-any.whl \
	&& apk del builddeps

WORKDIR /root

ENTRYPOINT [ "oci" ]
