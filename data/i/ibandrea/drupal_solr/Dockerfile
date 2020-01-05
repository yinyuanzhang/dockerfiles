FROM dockerimages/docker-solr:latest
MAINTAINER Andrea Lorenzetti <andrea@ibuildings.it>

ENV SOLR_START_VERSION=4.10.3
ENV DRUPAL_MODULE_VERSION=7.x-1.9
ENV DRUPAL_MODULE=search_api_solr-$DRUPAL_MODULE_VERSION.tar.gz

RUN set -x \
	&& wget -nv --output-document=/tmp/$DRUPAL_MODULE http://ftp.drupal.org/files/projects/$DRUPAL_MODULE \
	&& mkdir -p /tmp/src/ \
	&& tar xfz /tmp/$DRUPAL_MODULE -C /tmp/src/ \
	&& cp -f /tmp/src/search_api_solr/solr-conf/4.x/* /opt/solr/example/solr/collection1/conf/ \
	&& rm -rf /tmp/$DRUPAL_MODULE \
	&& rm -rf /tmp/src/
