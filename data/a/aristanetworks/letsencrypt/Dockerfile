# Copyright (c) 2017 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.
FROM aristanetworks/base:1.0
LABEL maintainer="Fabrice Rabaute fabrice@arista.com"

WORKDIR /root
ENV HOME /root

# Install nginx, certbot and kubectl
RUN export DEBIAN_FRONTEND=noninteractive \
  && add-apt-repository ppa:certbot/certbot \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    nginx \
    certbot \
    python-pip \
    python-setuptools \
  && rm -rf /var/lib/apt/lists/* \
  && rm /etc/nginx/sites-enabled/default \
  && wget -nv https://storage.googleapis.com/kubernetes-release/release/v1.13.2/bin/linux/amd64/kubectl \
  	-O /usr/local/bin/kubectl \
  && echo "96c123c1c7d90eb0cd7224efd10340f5fd714c85  /usr/local/bin/kubectl" | sha1sum -c - \
  && chmod +x /usr/local/bin/kubectl \
  && mkdir -p /var/www/letsencrypt \
  && chmod -R 755 /var/www/letsencrypt \
  && pip install certbot-dns-google

ENV HOME /home/${USER}
WORKDIR ${HOME}
