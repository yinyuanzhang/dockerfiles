FROM ubuntu:18.04

RUN groupadd -r bitcoin && useradd -r -m -g bitcoin bitcoin

RUN set -ex \
	&& apt-get update \
	&& apt-get install -y software-properties-common

RUN set -ex \
	&& apt-add-repository ppa:bitcoin/bitcoin \
	&& apt-get update \
	&& apt-get install -qq --no-install-recommends ca-certificates procps nano dirmngr gosu gpg wget bitcoind \
	&& rm -rf /var/lib/apt/lists/*

# create data directory
ENV BITCOIN_DATA /data
RUN mkdir $BITCOIN_DATA \
	&& chown -R bitcoin:bitcoin $BITCOIN_DATA \
	&& ln -sfn $BITCOIN_DATA /home/bitcoin/.bitcoin \
	&& chown -h bitcoin:bitcoin /home/bitcoin/.bitcoin
VOLUME /data

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8332 8333 18332 18333
CMD ["bitcoind", "-datadir=/home/bitcoin/.bitcoin", "--printoconsole"]
