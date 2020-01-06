FROM nginx@sha256:096c4b3464e2e465f20e9d704f1a0f8d27584df4d6758b6d00a14911cc9bb888

RUN apk add --no-cache tini openssl
COPY entrypoint.sh /
COPY default.conf /etc/nginx/conf.d/default.conf

WORKDIR /etc/nginx

ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]
