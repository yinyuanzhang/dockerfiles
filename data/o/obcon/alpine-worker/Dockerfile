FROM obcon/alpine-base

ADD rootfs /

RUN apk update && \
  apk upgrade && \
  apk add \
    nodejs && \
  rm -rf /var/cache/apk/*

RUN adduser -D worker && chown -R worker:worker /home/worker
WORKDIR /home/worker
USER worker
CMD [ "/usr/bin/node", "run.js" ]