FROM alpine
LABEL maintainer="recih"

RUN apk add --no-cache \
	bash \
    curl \
 && curl -L git.io/cow | bash \
 && apk del curl

COPY docker-initscript.sh /sbin/docker-initscript.sh
RUN chmod 755 /sbin/docker-initscript.sh

EXPOSE 7777/tcp
RUN mkdir /data
VOLUME /data

ENTRYPOINT ["bash", "/sbin/docker-initscript.sh"]
CMD ["cow"]
