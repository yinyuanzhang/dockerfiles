FROM alpine:3.8

RUN apk update && apk upgrade \
	&& apk add curl openssl ca-certificates bash git zip openssh-client rsync sshpass \
	&& rm -rf /var/cache/apk/*

RUN curl -fsSL https://goss.rocks/install | sh \
    && goss --version