FROM alpine:3.7

MAINTAINER Chris Every <eversmcc@gmail.com>

RUN apk add --no-cache bash ca-certificates curl openssl

ENV HELM_VERSION v2.9.0

RUN adduser -S helm helm

RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get > get_helm.sh
RUN chmod 700 get_helm.sh
RUN ./get_helm.sh --version $HELM_VERSION

USER helm
