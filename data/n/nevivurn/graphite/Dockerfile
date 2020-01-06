FROM nevivurn/base:latest

ARG WHISPER_VERSION=1.1.5
ARG CARBON_VERSION=1.1.5
ARG CARBON_API_VERSION=1.1.3

WORKDIR /tmp/build
RUN set -ex \
	&& apk update \
	# Install deps
	&& apk add -t .build-deps \
		build-base \
		libffi-dev \
		py2-pip \
		python2-dev \
	&& apk add -t .run-deps \
		cairo \
		py-setuptools \
		python2 \
	# Install whisper
	&& wget -O whisper.tar.gz "https://github.com/graphite-project/whisper/archive/${WHISPER_VERSION}.tar.gz" \
	&& mkdir whisper && tar -C whisper --strip-components=1 -xzf whisper.tar.gz && cd whisper \
	&& pip2 install --no-cache-dir -r requirements.txt && python2 setup.py install \
	&& cd .. \
	# Install carbon
	&& wget -O carbon.tar.gz "https://github.com/graphite-project/carbon/archive/${CARBON_VERSION}.tar.gz" \
	&& mkdir carbon && tar -C carbon --strip-components=1 -xzf carbon.tar.gz && cd carbon \
	&& pip2 install --no-cache-dir -r requirements.txt && python2 setup.py install \
	&& cd .. \
	# Install carbon-api
	&& wget -O carbon-api.tar.gz "https://github.com/brutasse/graphite-api/archive/${CARBON_API_VERSION}.tar.gz" \
	&& mkdir carbon-api && tar -C carbon-api --strip-components=1 -xzf carbon-api.tar.gz && cd carbon-api \
	&& pip2 install --no-cache-dir -r requirements.txt gunicorn && python2 setup.py install \
	# Cleanup
	&& cd .. \
	&& apk del .build-deps \
	&& rm -rf /tmp/build /var/cache/apk/*

COPY conf/ /opt/graphite/conf/
COPY service/ /docker/service/

WORKDIR /docker
EXPOSE 2003 8000
VOLUME /opt/graphite/storage/whisper
