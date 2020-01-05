FROM ubuntu:18.04
MAINTAINER Brad P. Crochet <brad@crochet.net>

RUN apt-get update && \
    apt-get install -y curl && \
    curl https://s3.amazonaws.com/beersmith-3/BeerSmith-3.0.9_amd64.deb -o /tmp/beersmith.deb && \
    apt-get install -y /tmp/beersmith.deb && \
    rm /tmp/beersmith.deb && \
    apt-get purge -y curl && \
    apt-get clean

RUN mkdir -p /home/beersmith3/.beersmith3 && \
    chmod 0775 -R /home/beersmith3

ENV HOME /home/beersmith3

CMD /usr/bin/beersmith3

