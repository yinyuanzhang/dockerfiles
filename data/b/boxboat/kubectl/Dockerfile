FROM alpine:3.7

RUN apk add --no-cache \
		curl

RUN curl -SsL -o /usr/local/bin/kubectl \
		"https://storage.googleapis.com/kubernetes-release/release/v1.12.3/bin/linux/amd64/kubectl" \
	&& chmod +x /usr/local/bin/kubectl

RUN addgroup -g 1000 alpine && \
    adduser -u 1000 -G alpine -h /home/alpine -s /bin/sh -D alpine

WORKDIR /home/alpine
USER alpine:alpine
ENTRYPOINT [ "/usr/local/bin/kubectl" ]
