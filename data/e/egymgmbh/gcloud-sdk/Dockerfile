FROM golang:latest AS build-env

ENV GO111MODULE on
RUN go get -v github.com/egymgmbh/kubejob
RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get > get_helm.sh && \
    chmod 700 get_helm.sh && \
    ./get_helm.sh
RUN curl https://get.helm.sh/helm-v3.0.1-linux-amd64.tar.gz --output helm-v3.0.1-linux-amd64.tar.gz \
    && echo "$(curl -s https://get.helm.sh/helm-v3.0.1-linux-amd64.tar.gz.sha256)" "helm-v3.0.1-linux-amd64.tar.gz" | sha256sum -c \
    && tar --strip-components 1 -xvf helm-v3.0.1-linux-amd64.tar.gz -C /usr/bin linux-amd64/helm
RUN git clone https://github.com/ahmetb/kubectx /opt/kubectx
ARG TF_VER=0.11.14
RUN curl https://releases.hashicorp.com/terraform/${TF_VER}/terraform_${TF_VER}_linux_amd64.zip > terraform_linux_amd64.zip \
    && gunzip -c terraform_linux_amd64.zip > /usr/bin/terraform \
    && chmod 700 /usr/bin/terraform

RUN apt-get update && apt-get install shellcheck -y
COPY tools /tools
WORKDIR /tools
RUN shellcheck *

FROM google/cloud-sdk:alpine

ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1
RUN gcloud components install kubectl \
    && echo "ipv6" >> /etc/modules \
    && apk --update add gettext

COPY tools/* /bin/
COPY --from=build-env /opt/kubectx/kubens /bin/
COPY --from=build-env /go/bin/kubejob     /bin/
RUN mkdir /bin/helm2 && mkdir /bin/helm3
COPY --from=build-env /usr/local/bin/helm /bin/helm2/
COPY --from=build-env /usr/bin/helm       /bin/helm3/
COPY --from=build-env /usr/bin/terraform  /bin/
