FROM solr:6.6.4

MAINTAINER Ivan Ermilov <ivan.s.ermilov@gmail.com>

ENV CKAN_VERSION 2.8.0

# Install CKAN Solr core
ADD ckan /ckan-configset

#RUN bin/solr solr-precreate -c ckan -d /ckan-configset
CMD ["solr-create", "-c", "ckan", "-d", "/ckan-configset"]
