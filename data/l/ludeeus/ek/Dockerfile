# Base image
FROM openjdk:8-jre-alpine

# Copy root filesystem
COPY rootfs /

# Versions
ENV ELASTIC_VERSION='6.7.1'
ENV S6_VERSION='1.22.1.0'

# ENV
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2

# Add apline 'edge'
RUN echo '@edge http://dl-cdn.alpinelinux.org/alpine/edge/main' >> /etc/apk/repositories

# Install packages
RUN apk add --no-cache \
    apk-tools=2.10.3-r1 \
    bash=4.4.19-r1 \
    curl=7.64.0-r1 \
    nodejs@edge \
    shadow \
    \
    && rm -f -r /tmp/* 

# Download and install s6-overlay
RUN curl -L -s https://github.com/just-containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz \
    | tar xvzf - -C / 

# Add ekuser
RUN useradd -ms /bin/bash ekuser

# Download and install elasticsearch
RUN curl -L -s https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-oss-${ELASTIC_VERSION}.tar.gz \
    | tar xvzf - -C /usr/local \
  && chown -R ekuser /usr/local/elasticsearch-${ELASTIC_VERSION}

# Download and install kibana
RUN curl -L -s https://artifacts.elastic.co/downloads/kibana/kibana-oss-${ELASTIC_VERSION}-linux-x86_64.tar.gz \
    | tar xvzf - -C /usr/local \
  && chown -R ekuser /usr/local/kibana-${ELASTIC_VERSION}-linux-x86_64

# fix node installation (https://github.com/elastic/kibana/issues/17015)
ENV KIBANA_DIR=/usr/local/kibana-${ELASTIC_VERSION}-linux-x86_64
RUN rm -rf ${KIBANA_DIR}/node \
  && mkdir -p ${KIBANA_DIR}/node/bin \
  && ln -s /usr/bin/node ${KIBANA_DIR}/node/bin/node

# Fix for Kibana issue with node
RUN sed -i 's/--max-http-header-size=65536//g' /usr/local/kibana-${ELASTIC_VERSION}-linux-x86_64/bin/kibana \
    && sed -i 's/!isVersionValid/isVersionValid/g' /usr/local/kibana-${ELASTIC_VERSION}-linux-x86_64/src/setup_node_env/node_version_validator.js

# Fix configuration
RUN sed -i 's/#server.host: "localhost"/server.host: "0.0.0.0"/g' /usr/local/kibana-${ELASTIC_VERSION}-linux-x86_64/config/kibana.yml
RUN sed -i 's/#network.host: 192.168.0.1/network.host: 0.0.0.0/g' /usr/local/elasticsearch-${ELASTIC_VERSION}/config/elasticsearch.yml



# Entrypoint
ENTRYPOINT [ "/init" ]

# Arguments
ARG BUILD_DATE

# Labels
LABEL \
    maintainer="Joakim Sørensen @ludeeus <ludeeus@gmail.com>" \
    org.label-schema.description="Elasticsearch and Kibana bundled in one container." \
    org.label-schema.name="EK" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.url="https://github.com/ludeeus/EK" \
    org.label-schema.usage="https://github.com/ludeeus/EK"