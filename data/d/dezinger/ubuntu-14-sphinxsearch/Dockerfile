FROM dezinger/ubuntu-14:latest

MAINTAINER dezinger@gmail.com

ENV DEBIAN_FRONTEND noninteractive

ARG SPHINX_VERSION=2.2.8-release
ARG DEBFILE=sphinxsearch_$SPHINX_VERSION-0ubuntu12~trusty_amd64.deb

COPY files/ /

RUN \ 
# install
    apt-get -y update && \
    apt-get install --no-install-recommends -y \ 
    wget cron odbcinst libpq5 odbcinst1debian2 libodbc1 unixodbc libmysqlclient18 && \
# http://sphinxsearch.com/downloads/archive/    
    wget http://sphinxsearch.com/files/$DEBFILE -O /tmp/$DEBFILE && \ 
    dpkg -i /tmp/$DEBFILE || true && rm -rf /tmp/$DEBFILE && \
# clean
    apt-get -y autoremove && apt-get -y clean && apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*