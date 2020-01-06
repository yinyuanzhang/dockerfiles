FROM dezinger/ubuntu-14-postgresql-9.3:latest

MAINTAINER dezinger@gmail.com

ENV DEBIAN_FRONTEND noninteractive

COPY files/ /

RUN \
    apt-get -y update && apt-get install --no-install-recommends -y \ 
# Install PostgreSQL addons
    postgresql-$PG_MAJOR-plproxy \ 
    skytools \ 
    skytools-modules-$PG_MAJOR \
    postgresql-plperl-$PG_MAJOR && \
# clean
    apt-get -y autoremove && apt-get -y clean && apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*