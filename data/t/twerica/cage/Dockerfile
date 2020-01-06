FROM docker/compose:1.23.2

RUN apk -U add \
  curl \
  zip \
  && rm -rf /var/cache/apk/*

RUN curl -L https://github.com/faradayio/cage/releases/download/v0.2.7/cage-v0.2.7-linux.zip > /tmp/cage.zip && \
  cd /tmp && \
  unzip cage.zip && \
  mv cage /usr/local/bin/cage && \
  rm -f /tmp/cage.zip

ENTRYPOINT sh
