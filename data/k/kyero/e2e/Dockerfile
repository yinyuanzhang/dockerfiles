FROM alpine:edge

LABEL maintainer "Kyero <dev@kyero.com>"

RUN addgroup -g 1000 node \
    && adduser -u 1000 -G node -s /bin/sh -D node

RUN mkdir -p /app

# Install base deps (with Chromium and Firefox)
RUN apk update && \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories &&  \
    apk add --no-cache --purge -u \
    nodejs nodejs-npm yarn \
    chromium firefox \
    xwininfo xvfb dbus eudev ttf-freefont fluxbox procps xvfb-run \
    nss freetype freetype-dev harfbuzz \
    ca-certificates wget

# Get glibc
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-2.29-r0.apk
RUN apk add glibc-2.29-r0.apk

# Get glibc-bin and glibc-i18n (required by BrowserStack Local)
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-bin-2.29-r0.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-i18n-2.29-r0.apk
RUN apk --update add glibc-bin-2.29-r0.apk glibc-i18n-2.29-r0.apk
RUN /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8

RUN apk add libstdc++

# Get BrowserStack Local
RUN wget https://www.browserstack.com/browserstack-local/BrowserStackLocal-linux-x64.zip \
    && unzip BrowserStackLocal-linux-x64.zip \
    && chmod +x BrowserStackLocal \
    && mv BrowserStackLocal /usr/local/bin \
    && rm BrowserStackLocal-linux-x64.zip

# Clear cache
RUN rm -rf /var/cache/apk/*

ENV CHROME_BIN=/usr/bin/chromium-browser \
    CHROME_PATH=/usr/lib/chromium/

# Copy install deps script
COPY install-deps /usr/local/bin/
RUN chmod +x /usr/local/bin/install-deps

WORKDIR /app

USER node

EXPOSE 1337 1338

# Install Node.js deps
ENTRYPOINT [ "install-deps" ]

CMD xvfb-run --server-num=99 --server-args='-ac -screen 0 1024x768x16' yarn test
