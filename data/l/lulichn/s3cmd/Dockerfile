FROM alpine:3.7

ADD entrypoint.sh /usr/local/bin/

RUN apk --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ add s3cmd \
	&& mkdir /data

WORKDIR /data
VOLUME /data

ENTRYPOINT ["entrypoint.sh"]
CMD ["--help"]

