FROM python:3.6-alpine

RUN apk update && apk upgrade \
	&& apk add --virtual .build-deps build-base libffi-dev openssl-dev \
	&& apk add libffi openssl \
	&& pip install --no-cache-dir pyaib \
 	&& apk del .build-deps \
 	&& mkdir -p /data /plugins

VOLUME /data
COPY entrypoint /entrypoint

CMD ["pyaib"]
ENTRYPOINT ["/entrypoint"]