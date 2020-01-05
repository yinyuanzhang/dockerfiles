FROM dabaopku/docker:Base

RUN apk upgrade --update && \
    apk add --no-cache mysql && \
	addgroup mysql mysql

VOLUME /var/lib/mysql
EXPOSE 3306

COPY run.sh /root
ENTRYPOINT ["/root/run.sh"]
