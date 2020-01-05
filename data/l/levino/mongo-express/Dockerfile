FROM node:0.12-slim

ENV TINI_VERSION 0.5.0
RUN set -x \
	&& apt-get update && apt-get install -y ca-certificates curl \
		--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* \
	&& curl -fSL "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini" -o /usr/local/bin/tini \
	&& chmod +x /usr/local/bin/tini \
	&& tini -h \
	&& apt-get purge --auto-remove -y ca-certificates curl

ENV MONGO_EXPRESS 0.28.4

RUN npm install mongo-express@$MONGO_EXPRESS

WORKDIR /node_modules/mongo-express

COPY config.js config.js

ENV ME_CONFIG_EDITORTHEME="default"
ENV ME_CONFIG_MONGODB_SERVER="mongo"
ENV ME_CONFIG_BASICAUTH_USERNAME=""
ENV ME_CONFIG_BASICAUTH_PASSWORD=""
ENV ME_CONFIG_PORT=8081
ENV ME_CONFIG_MONGODB_ADMIN_MODE="true"

EXPOSE 8081
CMD ["tini", "--", "node", "app"]
