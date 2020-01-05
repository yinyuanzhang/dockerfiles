# https://github.com/elastic/elasticsearch-docker
FROM docker.elastic.co/elasticsearch/elasticsearch-oss:6.5.4

COPY config/ config/
COPY bin/ bin/

RUN elasticsearch-plugin install --batch com.floragunn:search-guard-6:6.5.4-24.1 -v \
	&& chmod +x \
		plugins/search-guard-6/tools/hash.sh \
		plugins/search-guard-6/tools/sgadmin.sh

USER root
COPY ./es-entrypoint.sh /
RUN chmod +x /es-entrypoint.sh

USER elasticsearch
ENTRYPOINT ["/es-entrypoint.sh"]

