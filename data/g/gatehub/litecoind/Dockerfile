FROM debian:stable-slim

RUN useradd -r litecoin \
  && apt-get update -y \
  && apt-get install -y curl gnupg \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && set -ex \
  && for key in \
    B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    FE3348877809386C \
  ; do \
    gpg --no-tty --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" || \
    gpg --no-tty --keyserver pgp.mit.edu --recv-keys "$key" || \
    gpg --no-tty --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
    gpg --no-tty --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "$key" || \
    gpg --no-tty --keyserver keyserver.pgp.com --recv-keys "$key" ; \
  done

ENV GOSU_VERSION=1.11

RUN curl -o /usr/local/bin/gosu -fSL https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg --print-architecture) \
  && curl -o /usr/local/bin/gosu.asc -fSL https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg --print-architecture).asc \
  && gpg --verify /usr/local/bin/gosu.asc \
  && rm /usr/local/bin/gosu.asc \
  && chmod +x /usr/local/bin/gosu

ENV LITECOIN_VERSION=0.16.3
ENV LITECOIN_DATA=/home/litecoin/.litecoin
ENV LITECOIN_ABC_SHASUM="686d99d1746528648c2c54a1363d046436fd172beadaceea80bdc93043805994  litecoin-${LITECOIN_VERSION}-x86_64-linux-gnu.tar.gz"

RUN curl -SLO https://download.litecoin.org/litecoin-${LITECOIN_VERSION}/linux/litecoin-${LITECOIN_VERSION}-x86_64-linux-gnu.tar.gz \
  && echo "${LITECOIN_ABC_SHASUM}" | sha256sum -c \
  && tar --strip=2 -xzf *.tar.gz -C /usr/local/bin \
  && rm *.tar.gz

COPY litecoin.conf /home/litecoin/.litecoin/litecoin.conf
COPY docker-entrypoint.sh /entrypoint.sh

EXPOSE 9332 9333 19332 19443 19444

ENTRYPOINT ["/entrypoint.sh"]

CMD ["litecoind"]
