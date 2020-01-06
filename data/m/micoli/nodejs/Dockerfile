# the different stages of this Dockerfile are meant to be built into separate images
# https://docs.docker.com/compose/compose-file/#target

ARG NODE_VERSION=10

FROM node:${NODE_VERSION}-alpine

WORKDIR /app

RUN set -eux; \
	apk add --no-cache --virtual .build-deps \
		g++ \
		gcc \
		git \
		make \
		python

RUN set -eux; \
	apk add --no-cache --virtual .build-deps \
		npx
