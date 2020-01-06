FROM debian:stretch

RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y libgcc1:i386 wget

WORKDIR /tmp
RUN wget $(wget -O - https://planefinder.net/sharing/client | sed -e 's/.*"\(http:\/\/.*pfclient.*_i386.deb\).*/\1/;t;d' | sed 's/i386/amd64/')
RUN apt install $PWD/pfclient*.deb

COPY pfclient-config.json /etc/

COPY run-pfclient.sh /usr/local/bin/
RUN chmod 755 /usr/local/bin/run-pfclient.sh
CMD /usr/local/bin/run-pfclient.sh
