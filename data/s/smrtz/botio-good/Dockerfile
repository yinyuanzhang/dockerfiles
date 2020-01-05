FROM zencash/gosu-base:1.10

MAINTAINER cronicc@protonmail.com

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get --no-install-recommends -y install apt-utils \
    && DEBIAN_FRONTEND=noninteractive apt-get --no-install-recommends -y install git nodejs-legacy npm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN git clone -b UseCreds --single-branch https://github.com/ZencashOfficial/botio.git /root/botio \
    && cd /root/botio \
    && npm install -g

