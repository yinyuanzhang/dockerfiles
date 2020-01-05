# aquila/monetdb 

FROM ubuntu:16.04

MAINTAINER Andreas Lang <andreas.lang@aquilainsight.com>

ENV TERM="xterm" \
    ADMIN_PASSWORD="asdj.a5jdxx" \
    ANALYST_PASSWORD="ff9@dca489"

RUN apt-get update
RUN apt-get install -y \
    wget 

COPY monetdb.list /etc/apt/sources.list.d/monetdb.list
RUN wget --output-document=- https://www.monetdb.org/downloads/MonetDB-GPG-KEY | apt-key add -

RUN apt-get update
RUN apt-get install -y \
    monetdb5-sql \
    monetdb-client

COPY monetdb /var/lib/monetdb/.monetdb
RUN mkdir -p ~monetdb/dbfarm \
    && chmod 600 ~monetdb/.monetdb \
    && chown -R monetdb:monetdb ~monetdb

USER monetdb
RUN cat ~/.monetdb

RUN monetdbd create ~/dbfarm \
    && monetdbd start ~/dbfarm \
    && monetdb create ai_db \
    && monetdb set nclients=100 ai_db \
    && monetdb start ai_db \
    && monetdb release ai_db \
    && monetdbd set port=50000 ~/dbfarm \
    && monetdbd set control=yes ~/dbfarm \
    && monetdbd set listenaddr=0.0.0.0 ~/dbfarm \
    && monetdbd set passphrase=$PASSWORD ~/dbfarm \
    && monetdbd stop ~/dbfarm \
    && ln -sf /dev/stdout /var/lib/monetdb/dbfarm/merovingian.log

EXPOSE 50000

COPY monetdb.sh /var/lib/monetdb/monetdb.sh
CMD /var/lib/monetdb/monetdb.sh

