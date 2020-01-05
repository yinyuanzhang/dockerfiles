FROM travix/gocd-agent-gcloud-nodejs:18.12.0

MAINTAINER Travix

# Install pandoc and calibre for building the documentation site
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      pandoc \
      calibre \
    && apt-get clean -y \
    && apt-get autoclean -y \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && npm install -g babel-cli@6.26.0 babel-register@6.26.0 \
    && cd /usr/lib \
    && npm i git://github.com/Travix-International/l10ns.git
