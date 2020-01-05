FROM debian:jessie

RUN apt-get -qq update && \
apt-get install -qqy pbzip2 && \
apt-get -y clean && \
apt-get -y autoremove && \
rm -rf /var/lib/apt/lists/*

CMD /bin/bash
