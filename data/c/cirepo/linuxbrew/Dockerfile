
FROM alpine:3.8


ARG IMAGE_ARG_ALPINE_MIRROR


ENV ARIA2C_DOWNLOAD aria2c --file-allocation=none -c -x 10 -s 10 -m 0 --console-log-level=notice --log-level=notice --summary-interval=0


COPY --from=cirepo/glibc:2.23-r3-alpine-3.8-archive /data/root /


# adduser, usermod
# see: https://github.com/michaelsauter/docker-alpine/blob/master/Dockerfile
# 'alpine-sdk' or 'build-base' is the alpine equivalent to 'build-essential' or 'Development Tools'
# see: [What is the alpine equivalent to build-essential? #24](https://github.com/gliderlabs/docker-alpine/issues/24)
# see: https://github.com/Linuxbrew/brew/blob/master/Dockerfile
# see: https://github.com/Linuxbrew/brew/issues/403
# see: https://linuxbrew.sh/
RUN set -ex \
  && echo ===== Install libs and tools ===== \
  && echo "http://${IMAGE_ARG_ALPINE_MIRROR:-dl-cdn.alpinelinux.org}/alpine/v3.8/main" > /etc/apk/repositories \
  && echo "http://${IMAGE_ARG_ALPINE_MIRROR:-dl-cdn.alpinelinux.org}/alpine/v3.8/community" >> /etc/apk/repositories \
  && echo "http://${IMAGE_ARG_ALPINE_MIRROR:-dl-cdn.alpinelinux.org}/alpine/edge/testing/" >> /etc/apk/repositories \
  && apk add --update aria2 bash bzip2 ca-certificates curl git httpie jq nano openssl shadow sudo tar unzip vim wget xz \
  && apk add --update build-base file ruby ruby-irb ruby-json \
  && rm -r /var/cache/apk/* \
  && echo ===== Create user ===== \
  && addgroup -g 1000 linuxbrew \
  && adduser -h /home/linuxbrew -s /bin/bash -G linuxbrew -D -u 1000 linuxbrew \
  && usermod -a -G root linuxbrew \
  && echo "linuxbrew ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/linuxbrew \
  && chmod 0440 /etc/sudoers.d/linuxbrew \
  && chgrp -R linuxbrew /usr/local \
  && find /usr/local -type d | xargs chmod g+w

RUN mkdir -p /home/linuxbrew/.linuxbrew \
  && git clone https://github.com/Linuxbrew/brew.git /home/linuxbrew/.linuxbrew/Homebrew \
  && mkdir /home/linuxbrew/.linuxbrew/bin \
  && ln -s ../Homebrew/bin/brew /home/linuxbrew/.linuxbrew/bin/ \
  && chown -R linuxbrew: /home/linuxbrew/.linuxbrew

WORKDIR /home/linuxbrew
USER    linuxbrew
ENV HOME=/home/linuxbrew \
    PATH=/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:$PATH \
	SHELL=/bin/bash \
	USER=linuxbrew

# Install portable-ruby and tap homebrew/core.
RUN HOMEBREW_NO_ANALYTICS=1 HOMEBREW_NO_AUTO_UPDATE=1 brew tap homebrew/core \
	&& rm -rf ~/.cache
