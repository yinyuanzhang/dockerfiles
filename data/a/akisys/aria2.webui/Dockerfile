FROM nginx:mainline-alpine as build
RUN set -ex \
      && apk add --no-cache --no-progress wget ca-certificates
RUN set -ex \
      && wget -O /tmp/master.tar.gz https://github.com/ziahamza/webui-aria2/archive/master.tar.gz
RUN set -ex \
      && mkdir -p /app
RUN set -ex \
      && tar xf /tmp/master.tar.gz -C/app --strip-components=1

FROM nginx:mainline-alpine
RUN set -ex \
      && apk add --no-cache --no-progress run-parts
COPY --from=build /app /app
ENV \
  ARIA_RPC_HOST="localhost" \
  ARIA_RPC_SECRET="" \
  ARIA_RPC_PORT=6800
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
EXPOSE 80
STOPSIGNAL SIGTERM
COPY rootfs/ /
