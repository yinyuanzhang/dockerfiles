# Source: https://github.com/chrootLogin/iota-pm
FROM node:8-alpine

ARG IOTA_PM_VERSION=1.2.0

ENV IOTA_NODE="" \
  HTTP_PORT=8888 \
  HTTP_ADDRESS=0.0.0.0 \
  REFRESH=5

COPY root /

RUN apk --no-cache -U add \
  bash \
  su-exec \
  tini \
  && npm install -g iota-pm@${IOTA_PM_VERSION} \
  && chmod +x /docker-run.sh
  

VOLUME /opt/iota-pm

EXPOSE 8888

ENTRYPOINT ["/sbin/tini"]
CMD ["/docker-run.sh"]
