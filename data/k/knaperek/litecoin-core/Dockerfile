FROM debian:stretch-slim as builder

RUN set -ex \
	&& apt-get update \
	&& apt-get install -qq --no-install-recommends ca-certificates dirmngr gpg wget \
	&& rm -rf /var/lib/apt/lists/*

ENV LITECOIN_VERSION=0.17.1
ENV	LITECOIN_URL=https://download.litecoin.org/litecoin-$LITECOIN_VERSION/linux/litecoin-$LITECOIN_VERSION-x86_64-linux-gnu.tar.gz \
	LITECOIN_SHA256=9cab11ba75ea4fb64474d4fea5c5b6851f9a25fe9b1d4f7fc9c12b9f190fed07 \
	LITECOIN_ASC_URL=https://download.litecoin.org/litecoin-$LITECOIN_VERSION/SHA256SUMS.asc \
	LITECOIN_PGP_KEY=fe3348877809386c

RUN set -ex \
	&& cd /tmp \
	&& wget -qO litecoin.tar.gz "$LITECOIN_URL" \
	&& echo "$LITECOIN_SHA256 litecoin.tar.gz" | sha256sum -c - \
	&& gpg --no-tty --keyserver keyserver.ubuntu.com --recv-keys "$LITECOIN_PGP_KEY" \
	&& wget -qO litecoin.asc "$LITECOIN_ASC_URL" \
	&& gpg --verify litecoin.asc \
	&& tar -xzvf litecoin.tar.gz -C /usr/local --strip-components=1 --exclude=*-qt


FROM debian:stretch-slim
COPY --from=builder /usr/local/bin/litecoind /usr/local/bin/litecoin-cli /usr/local/bin/
RUN groupadd -r litecoin && useradd -r -m -g litecoin litecoin \
	&& ln -s /usr/local/bin/litecoin-cli /usr/local/bin/c

ENV LITECOIN_DATA=/data

# create data directory
RUN mkdir "$LITECOIN_DATA" \
	&& chown -R litecoin:litecoin "$LITECOIN_DATA" \
	&& ln -sfn "$LITECOIN_DATA" /home/litecoin/.litecoin \
	&& chown -h litecoin:litecoin /home/litecoin/.litecoin

VOLUME /data

COPY docker-entrypoint.sh /entrypoint.sh

USER litecoin

ENTRYPOINT ["/entrypoint.sh"]
CMD ["litecoind"]
