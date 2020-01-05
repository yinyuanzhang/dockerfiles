FROM debian:jessie

RUN apt-get update && apt-get install -y --no-install-recommends \
    default-jre \
    curl \
    lsof \
    wget \
    procps \
    unzip

ENV SOLR_VERSION 4.10.4
ENV SOLR solr-$SOLR_VERSION
ENV SOLR_USER solr

RUN groupadd -r $SOLR_USER && \
  useradd -r -g $SOLR_USER $SOLR_USER && \
  mkdir -p /opt && \
  wget -nv --output-document=/opt/$SOLR.tgz http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz && \
  tar -C /opt --extract --file /opt/$SOLR.tgz && \
  rm /opt/$SOLR.tgz && \
  ln -s /opt/$SOLR /opt/solr && \
  chown -R $SOLR_USER:$SOLR_USER /opt/solr /opt/$SOLR

EXPOSE 8983
WORKDIR /opt/solr

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash", "-c", "/opt/solr/bin/solr -f"]
