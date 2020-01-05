FROM ubuntu:16.04

ENV CONSTELLATION_VERSION=0.3.5
ENV QUORUM_VERSION=2.2.1
ENV TESSERA_VERSION=0.9.2
ENV TESSERA_LOC /usr/local/bin

# --------------------- path variables ---------------------
# geth data directory
ENV DATADIR=/run-quorum/blockchain/qdata/dd

# geth chain data directory
ENV CHAINDATADIR=/run-quorum/blockchain/qdata/dd/geth/chaindata

# geth genesis file
ENV GENESIS_FILE=/run-quorum/blockchain/genesis.json

# geth nodekey file
ENV NODEKEY=/run-quorum/blockchain/qdata/dd/geth/nodekey

# geth account password file
ENV PASSWORD=/run-quorum/blockchain/passwords.txt

# comma separated list of constellation public key files
ENV PUBLIC_KEYS=/run-quorum/constellation/keys/node.pub

# comma separated list of constellation private key files
ENV PRIVATE_KEYS=/run-quorum/constellation/keys/node.key

# constellation storage folder
ENV STORAGE=/run-quorum/constellation/storage

# constellation IPC file
ENV CONSTELLATION_IPC_FILE=/run-quorum/constellation/constellation.ipc

# tessera IPC file
ENV TESSERA_IPC_FILE=/run-quorum/tessera/tessera.ipc

# tessera json file
ENV TESSERA_JSON=/run-quorum/tessera/tessera.json

# to indicate
# geth account key folder
# to be populated with key file
ENV ACCOUNT_DIR=/run-quorum/blockchain/qdata/dd/keystore

# static (initial) nodes file
ENV STATIC_NODES=/run-quorum/blockchain/qdata/dd/static-nodes.json

# --------------------- geth variables ---------------------
# geth network id (must be integer > 1)
ARG networkid
ENV NETWORKID=$networkid

# Max allowed number of nodes in the network
ARG maxpeers=250
ENV MAXPEERS=$maxpeers

# geth listen port
ARG port=30303
ENV PORT=$port

# geth verbosity
ARG verbosity=2
ENV VERBOSITY=$verbosity

# geth RPC address to bind to (note: RPC has no authentication! Don't expose directly to public.)
ARG rpcaddr=0.0.0.0
ENV RPCADDR=$rpcaddr

# geth RPC listen port
ARG rpcport=8545
ENV RPCPORT=$rpcport

# geth RPC apis to enable
ARG rpcapi=admin,db,eth,debug,miner,net,shh,txpool,personal,web3,quorum,raft
ENV RPCAPI=$rpcapi

# Raft listen port
ARG raftport=50400
ENV RAFTPORT=$raftport

# --------------------- raft variables ---------------------
# Raft joining argument for *new* nodes only (an inetger id returned by any peer existing in the network)
ARG raftjoinexisting
ENV RAFTJOINEXISTING=$raftjoinexisting

# Inter-block time (in millisecs) interval for raft
ARG raftblocktime=50
ENV RAFTBLOCKTIME=$raftblocktime

# --------------------- ibft variables ---------------------
# Inter-block time (in secs) interval for ibft
ARG istanbulblocktime=1
ENV ISTANBUL_BLOCKPERIOD=$istanbulblocktime

# --------------------- common tessera/constellation variables ---------------------
# comma separated list of ptm peers
# e.g. https://35.198.219.161:9000/,https://25.98.111.101:9500/
ARG othernodes
ENV OTHERNODES=$othernodes

# --------------------- constellation variables ---------------------
# constellation bind address and port
# e.g. https://35.18.219.161:9000/
ARG constellation_url
ENV CONSTELLATION_URL=$constellation_url

# constellation port
ARG constellation_port=9000
ENV CONSTELLATION_PORT=$constellation_port

# Dependencies are for constellation
RUN apt-get update -qq \
    && apt-get install -qqy \
        wget \
        libleveldb-dev \
        libdb-dev \
        libtinfo-dev \
        zlib1g-dev \
        libsodium-dev \
        libgmp-dev \
        netbase \
    && apt-get clean

# Dependencies are for tessera
RUN apt-get install -y --no-install-recommends openjdk-8-jdk && \
    apt-get install -y --no-install-recommends ant

# Install constellation
RUN wget -q https://github.com/jpmorganchase/constellation/releases/download/v${CONSTELLATION_VERSION}-build.1/constellation-${CONSTELLATION_VERSION}-ubuntu1604.tar.gz  -O - \
    | tar xzO constellation-node > /usr/local/bin/constellation-node \
    && chmod +x /usr/local/bin/constellation-node

# Install tessera
RUN wget https://oss.sonatype.org/content/groups/public/com/jpmorgan/quorum/tessera-app/${TESSERA_VERSION}/tessera-app-${TESSERA_VERSION}-app.jar -O ${TESSERA_LOC}/tessera

# Install Quorum
RUN wget -q https://github.com/jpmorganchase/quorum/releases/download/v${QUORUM_VERSION}/geth_v${QUORUM_VERSION}_linux_amd64.tar.gz -O - \
    | tar xzO geth > /usr/local/bin/geth \
    && chmod +x /usr/local/bin/geth

# start script
COPY start_quorum_node.sh .

CMD ["/bin/bash", "start_quorum_node.sh"]
