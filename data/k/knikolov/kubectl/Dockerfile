FROM alpine:3.4

ENV KUBECTL_VERSION="v1.3.6"

RUN apk add --update ca-certificates openssh-client \
  jq curl bash git gcc g++ make libffi-dev openssl-dev \
  && curl -o /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \
  && chmod +x /usr/local/bin/kubectl \
  && apk add python python-dev py-pip build-base \
  && rm /var/cache/apk/* \
  && pip install requests pytest pykube
