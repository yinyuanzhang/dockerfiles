FROM elasticsearch:5.6

RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install --batch analysis-phonetic

RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install --batch analysis-icu

RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install --batch http://dl.bintray.com/content/imotov/elasticsearch-plugins/org/elasticsearch/elasticsearch-analysis-morphology/$ELASTICSEARCH_VERSION/elasticsearch-analysis-morphology-$ELASTICSEARCH_VERSION.zip

RUN echo -e "script.inline: on\nscript.indexed: on" >> /etc/elasticsearch/elasticsearch.yml

