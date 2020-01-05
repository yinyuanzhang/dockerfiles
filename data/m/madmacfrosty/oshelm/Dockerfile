from widerin/openshift-cli:v3.10.0

LABEL maintainer="Frosty <mick.frost@gmail.com>"

ENV HELM_LATEST_VERSION="v2.11.0"

RUN apk add --update ca-certificates \
 && apk add --update -t deps wget \
 && wget https://storage.googleapis.com/kubernetes-helm/helm-${HELM_LATEST_VERSION}-linux-amd64.tar.gz \
 && tar -xvf helm-${HELM_LATEST_VERSION}-linux-amd64.tar.gz \
 && mv linux-amd64/helm /usr/local/bin \
 && apk del --purge deps \
 && rm /var/cache/apk/* \
 && rm -f /helm-${HELM_LATEST_VERSION}-linux-amd64.tar.gz

RUN apk add --no-cache git bash && \
    mkdir -p "$(helm home)/plugins" && \
    helm plugin install https://github.com/databus23/helm-diff && \
    helm plugin install https://github.com/chartmuseum/helm-push && \
    helm plugin install https://github.com/futuresimple/helm-secrets && \
    apk del --purge git bash

RUN wget http://github.com/roboll/helmfile/releases/download/v0.40.1/helmfile_linux_amd64 && \
    mv helmfile_linux_amd64 /usr/local/bin/helmfile && \
    chmod u+x /usr/local/bin/helmfile

RUN apk add --update -t openssl

COPY bootstrap/ /bootstrap/
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["sh"]

