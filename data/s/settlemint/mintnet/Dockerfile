FROM parity/parity:v2.3.2

USER root

RUN apt-get update && apt-get install curl -y

RUN mkdir -p /mnt/io.parity.ethereum
VOLUME ["/mnt/io.parity.ethereum"]

ENTRYPOINT ["/entrypoint.sh"]

RUN mkdir -p /etc/mintnet
ADD ./reservedpeers.txt /etc/mintnet/reservedpeers.txt
ADD ./mintnet.toml /etc/mintnet/mintnet.toml
ADD ./mintnet.json /etc/mintnet/mintnet.json
ADD ./entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
