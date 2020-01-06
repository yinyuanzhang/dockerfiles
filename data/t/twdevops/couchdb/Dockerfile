FROM twdevops/base
MAINTAINER ShawnMa <qsma@thoughtworks.com>

## Add repository
RUN \
  add-apt-repository -y ppa:couchdb/stable

## Update and Install packages
RUN \
  apt-get update &&\
  apt-get install -y --no-install-recommends couchdb=1.6.1-0ubuntu2 pwgen

## Install configurations
ADD files/local.ini /etc/couchdb/local.ini
RUN \
  mkdir /var/run/couchdb &&\
  chown -R couchdb:couchdb /var/run/couchdb /etc/couchdb/local.*

## Install scripts
ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x     /entrypoint.sh

## Cleanup
RUN \
  apt-get autoclean -y &&\
  apt-get autoremove -y &&\
  rm -rf /tmp/*  &&\
  rm -rf /var/tmp/* &&\
  rm -rf /var/lib/apt/lists/*

EXPOSE 5984

WORKDIR /var/lib/couchdb

ENTRYPOINT ["/entrypoint.sh"]

VOLUME ["/var/lib/couchdb"]

CMD ["couchdb"]


