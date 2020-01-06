# Copyright 2015-2017 Ivan Krizsan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Elastalert Docker image running on Alpine Linux.
# Build image with: docker build -t ivankrizsan/elastalert:latest .

FROM python:3.6-alpine

LABEL maintainer="Francesco Ciocchetti <fciocchetti@mintel.com>" \
      version="0.2.1" \
      vcs-url="https://github.com/mintel/elastalert-docker"

# Set this environment variable to True to set timezone on container start.
ENV SET_CONTAINER_TIMEZONE False
# Default container timezone as found under the directory /usr/share/zoneinfo/.
ENV CONTAINER_TIMEZONE Etc/UTC
# VERSION from which to download Elastalert.
ENV ELASTALERT_VERSION "0.2.1"
# URL from which to download Elastalert.
ENV ELASTALERT_URL https://github.com/Yelp/elastalert/archive/v${ELASTALERT_VERSION}.zip
# Directory holding configuration for Elastalert and Supervisor.
ENV CONFIG_DIR /opt/config
# Elastalert rules directory.
ENV RULES_DIRECTORY /opt/rules
# Elastalert configuration file path in configuration directory.
ENV ELASTALERT_CONFIG ${CONFIG_DIR}/config.yaml
# Elastalert home directory full path.
ENV ELASTALERT_HOME /opt/elastalert
# Alias, DNS or IP of Elasticsearch host to be queried by Elastalert. Set in default Elasticsearch configuration file.
ENV ELASTICSEARCH_HOST elasticsearchhost
# Port on above Elasticsearch host. Set in default Elasticsearch configuration file.
ENV ELASTICSEARCH_PORT 9200
# Use TLS to connect to Elasticsearch (True or False)
ENV ELASTICSEARCH_TLS False
# Verify TLS
ENV ELASTICSEARCH_TLS_VERIFY True
# ElastAlert writeback index
ENV ELASTALERT_INDEX elastalert_status

WORKDIR /opt

# Install software required for Elastalert and NTP for time synchronization.
RUN apk update && \
    apk --no-cache upgrade && \
    apk --no-cache add ca-certificates openssl-dev openssl libffi-dev python3 python3-dev py3-pip py3-yaml gcc musl-dev tzdata openntpd wget libmagic && \
# Download and unpack Elastalert.
    wget -O elastalert.zip "${ELASTALERT_URL}" && \
    unzip elastalert.zip && \
    rm elastalert.zip && \
    mv elast* "${ELASTALERT_HOME}"

WORKDIR "${ELASTALERT_HOME}"

# Install Elastalert.
RUN python3 setup.py install && \
    pip3 install -e . && \
    pip3 uninstall twilio --yes && \
    pip3 install twilio==6.0.0 && \
    # 0.2.1 need patching for rule testing to work
    # see https://github.com/Yelp/elastalert/issues/2600
    sed -i -e 's/get_yaml(args.file)/load_yaml(args.file)/' /opt/elastalert/elastalert/test_rule.py && \
    # Create directories. The /var/empty directory is used by openntpd.
    mkdir -p "${CONFIG_DIR}" && \
    mkdir -p "${RULES_DIRECTORY}" && \
    mkdir -p /var/empty && \
    # Clean up.
    apk del python3-dev && \
    apk del musl-dev && \
    apk del gcc && \
    apk del openssl-dev && \
    apk del libffi-dev && \
    rm -rf /var/cache/apk/*

# Copy the script used to launch the Elastalert when a container is started.
COPY ./start-elastalert.sh /opt/
# Make the start-script executable.
RUN chmod +x /opt/start-elastalert.sh

# Define mount points.
VOLUME [ "${CONFIG_DIR}", "${RULES_DIRECTORY}" ]

# Launch Elastalert when a container is started.
CMD ["/opt/start-elastalert.sh"]
