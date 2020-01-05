FROM docker:18.06

RUN apk add --update -t deps curl tar gzip
RUN curl -L https://storage.googleapis.com/kubernetes-helm/helm-v2.9.1-linux-amd64.tar.gz > helm.tar.gz
RUN tar -zxvf helm.tar.gz
RUN mv linux-amd64/helm /usr/local/bin/helm
RUN rm -rf helm.tar.gz
RUN helm init --client-only
