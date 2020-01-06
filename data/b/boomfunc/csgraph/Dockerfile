# Final container, copy from builders
# Get pre-compiled base
FROM boomfunc/base:latest as base

ADD . /boomfunc/app

RUN set -ex \
	&& apk add --update --no-cache --virtual .run-deps \
		python \
	\
	&& apk add --update --no-cache --virtual .build-deps \
		py-pip \
	&& pip install --no-cache-dir -r requirements.txt \
	\
	&& rm -rf /var/cache/apk/* \
	&& apk del .build-deps
