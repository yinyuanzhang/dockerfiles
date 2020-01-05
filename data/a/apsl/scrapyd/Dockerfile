FROM apsl/circusbase
MAINTAINER Edu Herraiz <eherraiz@apsl.net>

VOLUME /data

# Things required for a python/pip environment
RUN  \
    apt-get update && \
    apt-get -y -q install git mercurial curl build-essential && \
    apt-get -y -q install python python-dev python-distribute python-pip && \
    apt-get -y -q install inetutils-ping dnsutils && \
    apt-get -y -q install libxml2-dev libxslt1-dev libssl-dev && \
    apt-get -y -q install libffi-dev && \
    apt-get clean

# install scrapyd
RUN pip --no-input install scrapyd==1.0.1

ADD conf/scrapyd.conf /etc/scrapyd/
ADD circus.d/scrapyd.ini /etc/circus.d/

# scrapyd
EXPOSE 6800
