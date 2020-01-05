FROM alpine:3.10

LABEL maintainer "Idealitsol <idealitsol@gmail.com>"

RUN apk update && apk add bash

ENV KUBE_LATEST_VERSION="v1.16.2"
ENV HELM_VERSION="v3.0.0"

RUN apk add --no-cache ca-certificates bash git openssh curl \
    && wget -q https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl \
    && wget -q https://get.helm.sh/helm-${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm \
    && chmod +x /usr/local/bin/helm

ENV HELM_HOME /tmp/helm 
RUN mkdir -p /tmp/helm
RUN helm init
RUN helm plugin install https://github.com/futuresimple/helm-secrets
RUN helm plugin install https://github.com/hypnoglow/helm-s3.git

USER root

COPY main /opt/idealitsol/bin/

ENV PATH="/opt/idealitsol/bin:$PATH"

ENTRYPOINT ["main"]

CMD ["--help"]
