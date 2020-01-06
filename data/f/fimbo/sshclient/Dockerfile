FROM alpine:latest

RUN apk update \
	&& apk add --no-cache openssh \
	&& apk add --no-cache sshpass \
	&& apk add --no-cache bash \
	&& apk add --no-cache git

RUN mkdir ~/.ssh \
	&& touch ~/.ssh/known_hosts