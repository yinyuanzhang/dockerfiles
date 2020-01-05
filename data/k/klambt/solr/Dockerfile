FROM solr:5-alpine
MAINTAINER Tim Weyand <tim.weyand@klambt.de>
USER root

COPY ./drupal-7/conf/* /opt/solr/server/solr/drupal7/conf/
COPY ./drupal-8/conf/* /opt/solr/server/solr/drupal8/conf/
RUN chown -R $SOLR_USER /opt/solr/server/solr/*

USER $SOLR_USER
RUN solr start \
 && /opt/solr/bin/solr create_core -c drupal7 \
 && /opt/solr/bin/solr create_core -c drupal8 

USER $SOLR_USER
EXPOSE 8983
CMD ["solr"]
