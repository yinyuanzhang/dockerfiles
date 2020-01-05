FROM parity/parity:v2.3.3

USER root

RUN apt-get update && apt-get install curl -y

ENTRYPOINT ["/entrypoint.sh"]

RUN mkdir -p /etc/mintnet
ADD ./dev.toml /etc/mintnet/dev.toml
ADD ./init.toml /etc/mintnet/init.toml
ADD ./dev.json /etc/mintnet/dev.json
ADD ./pwd.txt /etc/mintnet/pwd.txt
ADD ./entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh