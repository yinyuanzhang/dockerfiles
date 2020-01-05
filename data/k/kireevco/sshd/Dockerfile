FROM alpine:latest

LABEL maintainer="github.com/kireevco"

RUN apk update	&& apk upgrade && apk add openssh \
		&& sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \
		&& rm -rf /var/cache/apk/* /tmp/*

COPY docker-entrypoint.sh /usr/local/bin/

EXPOSE 22

ENTRYPOINT ["docker-entrypoint.sh"]
