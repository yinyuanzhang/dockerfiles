FROM alpine:3.5
MAINTAINER GoCD Contributors <go-cd-dev@googlegroups.com>

EXPOSE 5000

COPY . /cla-assistant
WORKDIR /cla-assistant

RUN \
  apk add --update nodejs su-exec git curl bzip2 patch make g++ && \
  addgroup -S cla-assistant && \
  adduser -S -D -G cla-assistant cla-assistant && \
  chown -R cla-assistant:cla-assistant /cla-assistant && \
  su-exec cla-assistant /bin/sh -c 'cd /cla-assistant && npm install && node_modules/grunt-cli/bin/grunt build && rm -rf /home/cla-assistant/.npm .git' && \
  apk del git curl bzip2 patch make g++

USER cla-assistant
CMD ["/bin/sh", "-c", "exec npm start > cla-assistant.log 2>&1"]
