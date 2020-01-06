FROM node:11-alpine

RUN set -ex \
		&& mkdir -p /srv

ADD . /srv

WORKDIR /srv

# trigger
RUN set -ex \
		&& apk add --no-cache \
			python2 \
			py-pip \
			curl \
		\
		&& npm config set unsafe-perm true \
		&& npm install node-sass \
		&& npm install -g \
		&& npm link \
		&& chmod +x ./serve.sh \
		\
		&& pip install awscli==1.15.4 \
		\
		&& apk del py-pip \
		&& rm -rf /tmp/* /var/cache/apk/*

ENTRYPOINT ["/srv/serve.sh"]
