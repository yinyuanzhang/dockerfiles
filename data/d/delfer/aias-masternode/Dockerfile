FROM ubuntu:16.04

RUN apt-get update \
 && apt-get -y install \
   wget \
   unzip \
   libzmq5 \
   libboost-system1.58.0 \
   libboost-filesystem1.58.0 \
   libboost-program-options1.58.0 \
   libboost-thread1.58.0 \
   libminiupnpc10 \
   libevent-pthreads-2.0-5 \
   libevent-2.0-5 \
   gettext-base \
   pwgen \
 && wget https://github.com/AIAScoinTechnologies/aiascoin/releases/download/1.2.0/aias1200-daemon.zip \
 && unzip aias1200-daemon.zip \
 && rm aias1200-daemon.zip \
 && mv aias* /bin \
 && chmod +x /bin/aias* \
 && wget https://cloudfront.debian.net/cdimage/snapshot/Debian/pool/main/d/db4.8/libdb4.8++_4.8.30-2_amd64.deb \
 && dpkg -i libdb4.8++_4.8.30-2_amd64.deb \
 && rm libdb4.8++_4.8.30-2_amd64.deb \
 && mkdir /data \
 && apt -y remove wget unzip \
 && rm -rf /var/lib/apt/lists/*

VOLUME /data

EXPOSE 10721

CMD [ \
   "/bin/bash", "-c", \
   "/bin/aiasd \
    -datadir=/data \
    -externalip=${IP} \
    -masternode=1 \
    -masternodeprivkey=${KEY} \
    -masternodeaddr=${IP}:${PORT:-10721} \
    -addnode=${ADD_NODE:-64.190.91.104} \
    -addnode=172.245.110.100 \
    -addnode=107.191.40.83 \
    -addnode=144.202.106.212 \
    -addnode=85.214.41.24 \
    -addnode=45.32.76.59 \
    -addnode=188.166.90.4 \
    -addnode=185.66.12.255 \
    -addnode=185.125.217.84 \
    -addnode=217.69.11.215 \
    -addnode=46.4.182.101 \
    -addnode=188.40.169.65 \
    -dnsseed=0 \
    -rpcallowip=0.0.0.0/0 \
    -rpcport=10720 \
    -rpcuser=aias-masternode-docker \
    -rpcpassword=${RPC_PASSWORD:-unsecurepassword} \
    -printtoconsole=1" \
]

