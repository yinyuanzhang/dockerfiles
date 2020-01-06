FROM ubuntu:16.04
MAINTAINER  aker
WORKDIR /root
RUN apt-get update  && \
        apt-get -y install wget libappindicator3-1 && \
	wget https://raw.githubusercontent.com/getlantern/lantern-binaries/master/lantern-installer-64-bit.deb && \
        dpkg -i lantern-installer-64-bit.deb && \
        rm -rf lantern-installer-64-bit.deb && \
        apt-get -f install && \
        apt-get clean && \
        rm -rf /var/cache/apt/* /var/lib/apt/lists/*

EXPOSE 3128/tcp 8080/tcp

ENTRYPOINT ["/usr/bin/lantern", "--configdir=/root", "--headless=true", "--proxyall=true", "--startup=false", "--clear-proxy-settings=false", "--addr=0.0.0.0:3128", "--uiaddr=0.0.0.0:8080"]
#/usr/bin/lantern --configdir=/root --headless=true --addr=0.0.0.0:3128  --uiaddr=0.0.0.0:8080 --proxyall=true --startup=false --clear-proxy-settings=false

