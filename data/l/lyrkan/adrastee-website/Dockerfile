FROM nginx:1.11-alpine

ARG HOST=adrastee.net

WORKDIR /srv/adrastee

COPY ./config /srv/adrastee/config
COPY ./src /srv/adrastee/src
COPY ./package.json /srv/adrastee/package.json
COPY ./yarn.lock /srv/adrastee/yarn.lock
COPY ./tsconfig.json /srv/adrastee/tsconfig.json
COPY ./tslint.json /srv/adrastee/tslint.json

# Install NodeJS/NPM + build app
RUN apk --update add --virtual \
		build-dependencies ca-certificates git musl-dev \
		nodejs autoconf automake libpng-dev gcc libtool \
		make nasm \
	&& npm install -g yarn \
	&& yarn install \
	&& yarn run build:prod \
	&& yarn cache clean \
	&& rm -fr node_modules \
	&& apk del build-dependencies

# Copy nginx conf
COPY docker/nginx/conf.d /etc/nginx/conf.d
