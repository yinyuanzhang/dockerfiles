FROM sebp/elk:670
ENV ES_HOME /opt/elasticsearch
WORKDIR ${ES_HOME}

#RUN CONF_DIR=/etc/elasticsearch gosu elasticsearch bin/elasticsearch-plugin install ingest-geoip
#RUN CONF_DIR=/etc/elasticsearch gosu elasticsearch bin/elasticsearch-plugin install ingest-user-agent
COPY kibana.yml /opt/kibana/config/