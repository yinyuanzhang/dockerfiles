FROM alpine:3.10

ENV \ 
  TEMPLE_VERSION=v0.3.0 \
  TEMPLE_SHA256=b804fcf08f07e2f9d7bea7fcac3c4ba3ec1f378d2616e3ce9827609f7490af9f

RUN \
  ## install tools \
  apk add --no-cache coreutils sed bash curl jq && \
  ## install temple \
  curl -o /usr/local/bin/temple -sSL https://github.com/docwhat/temple/releases/download/${TEMPLE_VERSION}/temple_linux_amd64 && \
  cd /usr/local/bin && printf "${TEMPLE_SHA256}  temple" | sha256sum -c && chmod 755 temple && \
  ## set bash as the default shell for root \
  sed -i '\~root:x:0:0~ { s~/bin/ash~/bin/bash~ }' /etc/passwd && \
  ## clean up \
  rm -rf /tmp/*.apk

CMD ["/bin/bash"]
