FROM parity/parity:stable

USER root

# Install curl
RUN apt-get update && apt-get install curl -y

# Change the db path
RUN mkdir -p /mnt/io.parity.ethereum

VOLUME ["/mnt/io.parity.ethereum"]

RUN mkdir -p /etc/parityPoA
ADD ./configPoAInit.toml /etc/parityPoA/configPoAInit.toml
ADD ./configPoANode.toml /etc/parityPoA/configPoANode.toml
ADD ./PoA.json /etc/parityPoA/PoA.json
ADD ./entrypoint.sh /entrypoint.sh

# For the signer
RUN mkdir -p ~/.local/share/io.parity.ethereum/signer

ENTRYPOINT ["/entrypoint.sh"]