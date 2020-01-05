FROM parity/parity:v2.5.8-stable

USER root

COPY --chown=parity ./parity/config /parity/config

COPY --chown=parity ./parity/authorities/authority.json /home/parity/.local/share/io.parity.ethereum/keys/DevelopmentChain/authority.json

COPY --chown=parity ./parity/authorities/authority.pwd /parity/authorities/authority.pwd

COPY --chown=parity ./parity/node.network.key /home/parity/.local/share/io.parity.ethereum/network/key

RUN mkdir -p /home/parity/.local/share/io.parity.ethereum/chains/DevelopmentChain/db

RUN chown -R parity: /home/parity/.local/share/io.parity.ethereum

USER parity