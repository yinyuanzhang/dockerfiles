FROM docker.elastic.co/elasticsearch/elasticsearch:6.4.0
RUN elasticsearch-plugin install analysis-stempel
CMD [ "bin/elasticsearch", "-Ediscovery.type=single-node" ]
