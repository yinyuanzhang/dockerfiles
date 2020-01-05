FROM alpine

RUN \
  apk update && \
  apk add bash py-pip curl bind-tools && \
  apk add --virtual=build gcc libffi-dev musl-dev openssl-dev python-dev make && \
  pip install azure-cli && \
  apk del --purge build
ARG kubectl_version=v1.11.1
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$kubectl_version/bin/linux/amd64/kubectl && chmod +x kubectl && mv kubectl /usr/local/bin/

