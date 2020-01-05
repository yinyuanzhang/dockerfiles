FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.16


RUN bin/elasticsearch-plugin install repository-s3 --batch


RUN bin/elasticsearch-plugin install repository-azure --batch
