FROM google/cloud-sdk:219.0.1-alpine

MAINTAINER Simone La Placa <simone.laplaca@crweb.it>

ENV HELM_VERSION v2.13.0
ENV KUBECTL_VERSION v1.13.4
ENV FILENAME helm-${HELM_VERSION}-linux-amd64.tar.gz

WORKDIR /

# install helm
ADD https://storage.googleapis.com/kubernetes-helm/${FILENAME} /tmp

RUN tar -zxvf /tmp/${FILENAME} -C /tmp \
  && mv /tmp/linux-amd64/helm /bin/helm \
  && chmod 755 /bin/helm \
  && chown root:root /bin/helm \
  && rm -rf /tmp
  
# install kubectl
ADD https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl /tmp/kubectl

RUN mv /tmp/kubectl /bin/kubectl \
    && chmod 755 /bin/kubectl \
    && chown root:root /bin/kubectl

RUN helm init --client-only
