FROM golang:alpine AS mustache

RUN apk add git

RUN go get github.com/cbroglie/mustache/...

FROM maven:3.6.0-jdk-8-alpine

COPY --from=mustache /go/bin/mustache /usr/local/bin/mustache

COPY scripts/pre-mvn-entrypoint.sh /usr/local/bin/pre-mvn-entrypoint.sh
COPY scripts/env_to_settings.sh /usr/local/bin/env_to_settings
COPY scripts/settings.xml.mustache /etc/env_to_settings/settings.xml.mustache

RUN apk --no-cache --update-cache add \
        bash \
        curl \
        openssh-client \
        jq \
        git \
        py-pip \
        python &&\
    pip install --upgrade \
      pip \
      yq

ENTRYPOINT ["/usr/local/bin/pre-mvn-entrypoint.sh"]

CMD ["mvn", "--version"]
