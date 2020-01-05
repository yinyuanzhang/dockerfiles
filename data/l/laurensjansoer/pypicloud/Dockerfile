FROM python:3.7.0-alpine3.8
MAINTAINER Laurens-Jan Soer

# After:
# - https://github.com/cirocosta/alpine-envsubst
# - https://github.com/stevearc/pypicloud-docker/tree/master/py3-alpine

EXPOSE 8080
WORKDIR /app/

# Install packages required
ENV PYPICLOUD_VERSION 1.0.9
ENV PLUGINS server,gcs,redis
RUN apk add --no-cache --virtual build-deps gettext python3-dev build-base linux-headers openldap-dev && \
	apk add --no-cache libintl libldap libpq util-linux-dev libffi-dev && \
	pip install pypicloud[$PLUGINS]==$PYPICLOUD_VERSION requests uwsgi pastescript && \
	cp /usr/bin/envsubst /usr/local/bin/envsubst && \
	adduser -D -s /bin/sh -h /var/lib/pypicloud/ pypicloud && \
	apk del --no-cache build-deps

# Create a working directory for pypicloud
VOLUME /var/lib/pypicloud

ADD ./run.sh /run.sh
RUN chmod +x /run.sh

# Run as pypicloud user
USER pypicloud

CMD ["/bin/sh", "/run.sh"]