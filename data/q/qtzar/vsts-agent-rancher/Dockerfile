FROM microsoft/vsts-agent:ubuntu-16.04-docker-17.06.0-ce-standard
MAINTAINER Declan Lynch <dlynch@qtzar.com>

ENV RANCHER_CLI_VERSION 0.6.9

RUN set -x \
  && apt-get update \
  && apt-get install -y --no-install-recommends python-pip python-dev python-setuptools build-essential \
  && pip install --upgrade pip \
  && pip install --upgrade virtualenv \
  && pip install requests==2.18.4 \
  && pip install baker==1.3 \
  && pip install websocket-client==0.44.0 \
  && apt-get remove -y python-pip \
  && rm -rf /var/lib/apt/lists/* \
  && curl -sL https://raw.githubusercontent.com/etlweather/gaucho/master/services.py -o rancher.py \
  && mv rancher.py /usr/bin/rancher.py \
  && chmod +x /usr/bin/rancher.py \
  && curl -sL https://github.com/rancher/cli/releases/download/v${RANCHER_CLI_VERSION}/rancher-linux-amd64-v${RANCHER_CLI_VERSION}.tar.gz -o rancher-linux-amd64-v${RANCHER_CLI_VERSION}.tar.gz \
  && tar xvfz rancher-linux-amd64-v${RANCHER_CLI_VERSION}.tar.gz \
  && cp rancher-v${RANCHER_CLI_VERSION}/rancher /usr/bin/rancher \
  && rm -rf rancher* \
  && chmod +x /usr/bin/rancher
