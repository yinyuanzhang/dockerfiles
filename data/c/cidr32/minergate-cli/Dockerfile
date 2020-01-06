# Forked from minecoins/docker-minergate-cli (https://github.com/minecoins/docker-minergate-cli)

FROM ubuntu:16.04
LABEL Maintainer="cidr32" \
      Description="Unofficial Docker image for minergate-cli."

# global env
ENV MINERGATE_INSTALL="https://download.minergate.com/ubuntu-cli"

# user env
# ENV USERNAME email@email.com
# ENV CURRENCY xmr

# install packages
RUN \
apt-get update && \
apt-get -qq --no-install-recommends install \
ca-certificates \
wget \
curl

# install miner
RUN \
wget -q --content-disposition "$MINERGATE_INSTALL" && \
dpkg -i *.deb || true && \

# install cleanup
apt-get -f -y install && \
apt-get -y autoremove && \
apt-get -y clean && \
rm -rf /var/lib/apt/lists/* && \
rm -rf /tmp/* && \
rm -rf /var/tmp/*

ENTRYPOINT ["minergate-cli"]

CMD ["minergate-cli", "--user", "sandboxboxmining@gmail.com", "--xmr"]
