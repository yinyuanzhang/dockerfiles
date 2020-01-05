FROM alpine:3.10

ARG RELEASE
RUN \
  ## install tools \
  apk add --no-cache coreutils sed bash curl jq && \
  ## install kafka connect cli \
  cd /tmp && _v=$RELEASE && _file=kafka-connect-$_v-linux-amd64.tar.gz && \
    curl -sSLO https://github.com/go-kafka/connect/releases/download/cli-$_v/$_file && \
    curl -sSLO https://github.com/go-kafka/connect/releases/download/cli-$_v/$_file.sha256sum && \
    sha256sum -c $_file.sha256sum && tar -xzf $_file && \
    cp /tmp/linux-amd64/kafka-connect /usr/local/bin && rm -rf /tmp/linux-amd64 /tmp/$_file /tmp/$_file.sha256sum && \
  ## set bash as the default shell for root \
  sed -i '\~root:x:0:0~ { s~/bin/ash~/bin/bash~ }' /etc/passwd && \
  ## clean up \
  rm -rf /tmp/*.apk

CMD ["/bin/bash"]
