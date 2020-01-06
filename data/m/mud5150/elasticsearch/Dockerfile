FROM docker.elastic.co/elasticsearch/elasticsearch:7.2.0
RUN mkdir /local && touch /local/unicast_hosts.txt && ln -s /local/unicast_hosts.txt /usr/share/elasticsearch/config/unicast_hosts.txt
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install -b "https://d3g5vo6xdbdb9a.cloudfront.net/downloads/elasticsearch-plugins/opendistro-security/opendistro_security-1.2.0.0.zip"
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install -b https://d3g5vo6xdbdb9a.cloudfront.net/downloads/elasticsearch-plugins/opendistro-alerting/opendistro_alerting-1.2.0.0.zip
