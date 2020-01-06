FROM node:10-alpine

ENV PATH /root/.local/bin:$PATH
RUN apk add \
		bash \
		curl \
		git \
		openssh-client \
		rsync \
	&& \
	rm -rf /var/cache/apk/*

COPY scripts /root/.local/bin
RUN chmod +x /root/.local/bin/*
