FROM alpine:3.2
MAINTAINER Didiet Noor <dnoor@kulina.id> (@lynxluna)

ENV TERM=dumb
ENV VERSION=v5.10.1 NPM_VERSION=3

ENV CONFIG_FLAGS="--without-npm" DEL_PKGS="g++ gcc libgcc libstdc++" RM_DIRS=/usr/include


# Patch APK Mirror to YKode
RUN echo "https://alpine.ykode.com/alpine/v3.2/main" > /etc/apk/repositories

RUN apk add --update curl make gcc g++ binutils-gold python linux-headers paxctl libgcc libstdc++ && \
  curl -sSL https://nodejs.org/dist/${VERSION}/node-${VERSION}.tar.gz | tar -xz && \
  cd /node-${VERSION} && \
  ./configure --without-snapshot --prefix=/usr ${CONFIG_FLAGS} && \
  make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \
  make install && \
  paxctl -cm /usr/bin/node && \
  cd / && \
  if [ -x /usr/bin/npm ]; then \
    npm install -g npm@${NPM_VERSION} && \
    find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm -rf; \
  fi && \
  apk del curl make clang binutils-gold python linux-headers paxctl ${DEL_PKGS} && \
  rm -rf /etc/ssl /node-${VERSION} ${RM_DIRS} \
    /usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp \
    /usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html

