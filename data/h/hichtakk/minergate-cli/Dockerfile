FROM ubuntu:18.04
RUN set -x && \
    apt-get update && \
    apt-get install -y wget && \
    wget https://minergate.com/download/ubuntu-cli -P /tmp && \
    apt-get install -y libbsd0 libpcre16-3 libssl1.0-dev libxau6 libxcb1 libxdmcp6 multiarch-support && \
    dpkg -i /tmp/ubuntu-cli && \
    rm /tmp/ubuntu-cli

CMD /usr/bin/minergate-cli -u ${USER} --${CURRENCY}
