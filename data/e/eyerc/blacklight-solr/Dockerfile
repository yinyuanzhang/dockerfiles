FROM solr:6.6
LABEL maintainer="Cort Eyer"
# Forked from University of Alberta Libraries
COPY ./solr/blacklight-core/conf /myconfig
COPY ./solr/lib /opt/solr/lib

USER root

RUN apt-get update
RUN apt-get --assume-yes install vim nano

USER solr

CMD ["solr-precreate", "discovery", "/myconfig"]
RUN bin/solr -e dih -p 8984
