FROM ubuntu:trusty

RUN \
    apt-get update \
        --quiet \
    && apt-get install \
        --yes \
        --no-install-recommends \
        --no-install-suggests \
    software-properties-common \
    python-software-properties \

# Clean up packages.
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add Java.
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Install Elasticsearch.
ENV ES_PKG_NAME elasticsearch-1.5.0

RUN \
  cd / && \
  wget https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz && \
  tar xvzf $ES_PKG_NAME.tar.gz && \
  rm -f $ES_PKG_NAME.tar.gz && \
  mv /$ES_PKG_NAME /elasticsearch

# Set up default Elasticsearch config.
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml

# Elasticsearch http-basic plugin.
ENV HTTP_BASIC_URL https://github.com/Asquera/elasticsearch-http-basic/releases/download/v1.5.0/elasticsearch-http-basic-1.5.0.jar
RUN /elasticsearch/bin/plugin --url $HTTP_BASIC_URL --install http-basic-server-plugin

# Elasticsearch mapper-attachments plugin.
RUN /elasticsearch/bin/plugin install elasticsearch/elasticsearch-mapper-attachments/2.5.0

# Elasticsearch elasticsearch-cloud-aws plugin.
RUN /elasticsearch/bin/plugin install elasticsearch/elasticsearch-cloud-aws/2.5.1

# Set up prep script location.
ADD scripts /scripts
RUN chmod +x /scripts/*.sh
RUN touch /.firstrun

# Mount for persistent data.
WORKDIR /data

ENTRYPOINT ["/bin/bash", "/scripts/start.sh"]
CMD [""]

EXPOSE 9200 9300

VOLUME ["/data"]
