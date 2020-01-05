# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.
FROM aristanetworks/base:1.0
LABEL maintainer="Fabrice Rabaute fabrice@arista.com"

ENV CURATOR_VERSION 5.8.1

# Install curator
RUN export DEBIAN_FRONTEND=noninteractive \
  && wget -nv https://packages.elastic.co/curator/5/debian/pool/main/e/elasticsearch-curator/elasticsearch-curator_${CURATOR_VERSION}_amd64.deb \
    -O elasticsearch-curator_amd64.deb \
  && echo "7d7510d534a55bc040995e59a44d94fa5e1616a5  elasticsearch-curator_amd64.deb" | sha1sum -c - \
  && dpkg -i elasticsearch-curator_amd64.deb \
  && rm elasticsearch-curator_amd64.deb

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ENTRYPOINT ["/usr/bin/dumb-init", "--", "curator"]
