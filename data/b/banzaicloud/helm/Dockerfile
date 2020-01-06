FROM alpine:3.9

ENV HELM_VERSION "v2.16.1"
ENV HELM_HOME "/.helm"

RUN apk add --update ca-certificates git openssl openssh py-pip findutils bash curl

RUN pip install --upgrade pip && pip install s3cmd

RUN curl -q https://raw.githubusercontent.com/helm/helm/master/scripts/get | bash -s -- --version $HELM_VERSION

RUN mkdir -p $HELM_HOME/plugins

RUN helm plugin install https://github.com/chartmuseum/helm-push

RUN helm init -c
RUN helm repo remove local
