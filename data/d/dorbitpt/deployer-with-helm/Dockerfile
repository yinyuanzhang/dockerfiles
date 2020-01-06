FROM dorbitpt/deployer:1.17

RUN apk --update --no-cache add tar jq perl

ENV HELM_VERSION v3.0.2

RUN curl -LO "https://get.helm.sh/helm-${HELM_VERSION}-linux-amd64.tar.gz"
RUN tar -zxvf "helm-${HELM_VERSION}-linux-amd64.tar.gz"
RUN mv linux-amd64/helm /usr/local/bin/helm