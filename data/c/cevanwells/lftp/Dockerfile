FROM alpine:3.10
LABEL maintainer "Chris Wells <chris@cevanwells.com>"

RUN apk add --no-cache lftp

ENV APP_DIR=/app
ENV APP_SHARE_DIR=/usr/local/share/lftp
ENV FTP_IP="IP ADDRESS"
ENV FTP_USER="FTP USERNAME"
ENV FTP_PASS="FTP PASSWORD"

WORKDIR $APP_DIR
RUN mkdir config data

COPY bin/* /usr/local/bin/

RUN addgroup -S appworker \
	&& adduser -D -S -H -h $APP_DIR -G appworker appworker \
	&& chown appworker:appworker -R $APP_DIR

RUN chmod +x /usr/local/bin/*.sh
USER appworker
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["/usr/local/bin/docker-cmd.sh"]