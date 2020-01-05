FROM alpine:3.9

ENV VERSION v2.12.1

MAINTAINER Jeremy Mouton <moutonjeremy@labbs.fr>

WORKDIR /

RUN apk --update add ca-certificates wget python curl tar

ENV FILENAME helm-${VERSION}-linux-amd64.tar.gz
ENV HELM_URL https://storage.googleapis.com/kubernetes-helm/${FILENAME}

RUN curl -o /tmp/$FILENAME ${HELM_URL} \
    && tar -zxvf /tmp/${FILENAME} -C /tmp \
    && mv /tmp/linux-amd64/helm /bin/helm \
    && rm -rf /tmp

RUN apk --update add git bash make

RUN helm init --client-only

RUN helm plugin install https://github.com/hypnoglow/helm-s3.git
