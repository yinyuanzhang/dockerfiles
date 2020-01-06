# Using alpine Linux - latest
FROM alpine:latest

LABEL maintainer="Sanny Mulyono <smulyono@me.com>"

RUN apk update && \
	apk add --update net-tools git bash vim sudo netcat-openbsd

CMD ["/bin/bash"]