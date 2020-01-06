FROM java:8-jre

# grab gosu for easy step-down from root
RUN apt-get upgrade -y \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& arch="$(dpkg --print-architecture)" \
	&& set -x \
	&& curl -o /usr/local/bin/gosu -fSL "https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch" \
	&& curl -o /usr/local/bin/gosu.asc -fSL "https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch.asc" \
	&& gpg --verify /usr/local/bin/gosu.asc \
	&& rm /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu \
	&& apt-get install -y wget \
	&& rm -rf /var/lib/apt/lists/*

ENV ELASTICSEARCH_MAJOR 2.3
ENV ELASTICSEARCH_VERSION 2.3.1
ENV ELASTICSEARCH_REPO_BASE http://packages.elasticsearch.org/elasticsearch/2.x/debian
ENV PATH /usr/share/elasticsearch/bin:$PATH

# https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-repositories.html
# https://packages.elasticsearch.org/GPG-KEY-elasticsearch
#RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys 46095ACC8548582C1A2699A9D27D666CD88E42B4
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add - \
	&& echo "deb $ELASTICSEARCH_REPO_BASE stable main" > /etc/apt/sources.list.d/elasticsearch.list

RUN set -x \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends elasticsearch=$ELASTICSEARCH_VERSION \
	&& rm -rf /var/lib/apt/lists/* \
	&& plugin install lmenezes/elasticsearch-kopf/2.0 \
	&& plugin install analysis-icu \
	&& plugin install delete-by-query

RUN set -ex \
	&& for path in \
		/usr/share/elasticsearch/data \
		/usr/share/elasticsearch/logs \
		/usr/share/elasticsearch/config \
		/usr/share/elasticsearch/config/scripts \
		/usr/share/elasticsearch/config/hunspell \
		/usr/share/elasticsearch/config/hunspell/cs_CZ \
	; do \
		mkdir -p "$path"; \
		chown -R elasticsearch:elasticsearch "$path"; \
	done

COPY elastic /usr/share/elasticsearch/config

VOLUME /usr/share/elasticsearch/data

COPY elastic/docker-entrypoint.sh /

EXPOSE 9200 9300
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]
