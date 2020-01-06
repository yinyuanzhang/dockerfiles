FROM alpine:3.3

RUN set -x \
  && apk --update --no-cache add ruby ruby-rdoc ruby-irb nodejs \
  && gem install sass \
  && npm install -g grunt \
  && adduser -u 501 -D dinghy # Make it possible to run `npm install` in shared directory via dinghy NFS.

WORKDIR /app
