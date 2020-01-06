FROM alpine as prep

ENV JTS_VERSION=1.15.0
ENV DDF_VERSION=2.14.0-SNAPSHOT
ENV DDF_REPO=snapshots
ENV DDF_ARTIFACT_URL="https://artifacts.codice.org/service/local/artifact/maven/content?r=$DDF_REPO&v=$DDF_VERSION"
ENV CONFIG_SRC=/configs
ENV CORE_DEST=/cores

RUN apk add --no-cache curl
RUN mkdir -p /deps /plugins /configs /cores/catalog/conf /cores/metacard_cache/conf /cores/alerts/conf
RUN curl -Ls "http://central.maven.org/maven2/org/locationtech/jts/jts-core/$JTS_VERSION/jts-core-$JTS_VERSION.jar" -o "/deps/jts-core-$JTS_VERSION.jar"
RUN curl -Ls "$DDF_ARTIFACT_URL&g=ddf.platform.solr&a=solr-xpath" -o "/plugins/solr-xpath-$DDF_VERSION.jar"
RUN curl -Ls "$DDF_ARTIFACT_URL&g=ddf.platform.solr&a=platform-solr-server-standalone&c=protwords&p=txt" -o "/configs/protwords.txt"
RUN curl -Ls "$DDF_ARTIFACT_URL&g=ddf.platform.solr&a=platform-solr-server-standalone&c=schema&p=xml" -o "/configs/schema.xml"
RUN curl -Ls "$DDF_ARTIFACT_URL&g=ddf.platform.solr&a=platform-solr-server-standalone&c=solr&p=xml" -o "/configs/solr.xml"
RUN curl -Ls "$DDF_ARTIFACT_URL&g=ddf.platform.solr&a=platform-solr-server-standalone&c=solrconfig&p=xml" -o "/configs/solrconfig.xml"
RUN curl -Ls "$DDF_ARTIFACT_URL&g=ddf.platform.solr&a=platform-solr-server-standalone&c=solrconfig-inmemory&p=xml" -o "/configs/solrconfig-inmemory.xml"
RUN curl -Ls "$DDF_ARTIFACT_URL&g=ddf.platform.solr&a=platform-solr-server-standalone&c=stopwords_en&p=txt" -o "/configs/stopwords_en.txt"
RUN curl -Ls "$DDF_ARTIFACT_URL&g=ddf.platform.solr&a=platform-solr-server-standalone&c=stopwords&p=txt" -o "/configs/stopwords.txt"
RUN curl -Ls "$DDF_ARTIFACT_URL&g=ddf.platform.solr&a=platform-solr-server-standalone&c=synonyms&p=txt" -o "/configs/synonyms.txt"

RUN apk add --no-cache bash

COPY scripts/createCore.sh /usr/local/bin/create-core
RUN create-core catalog
RUN create-core metacard_cache
RUN create-core alerts

FROM solr:7.4.0

COPY --from=prep /deps/*.jar /opt/solr/server/lib/
COPY --from=prep /plugins/*.jar /opt/solr/plugins/
COPY --from=prep /cores/ /opt/solr/server/solr/
USER root
RUN chown -R solr:solr /opt/solr/plugins
RUN chown -R solr:solr /opt/solr/server/solr
USER solr
