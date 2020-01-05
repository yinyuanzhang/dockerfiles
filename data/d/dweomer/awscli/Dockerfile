FROM alpine:3.7

ARG PKG_BUILD="py-pip"
ARG PKG_EXTRA="bash bind-tools ca-certificates curl jq less wget"

RUN set -x \
 && apk add --update --no-cache \
    groff \
    py-setuptools \
    python \
    $PKG_BUILD \
    $PKG_EXTRA \
 && pip --no-cache-dir install awscli \
 && wget -qP ~/.aws/cli 'https://raw.githubusercontent.com/awslabs/awscli-aliases/master/alias' \
 && apk del $PKG_BUILD \
 && aws --version

ENTRYPOINT ["aws"]
CMD ["whoami"]

LABEL org.label-schema.name="dweomer/awscli" \
      org.label-schema.description="AWS CLI on Alpine" \
      org.label-schema.url="https://github.com/dweomer/dockerfiles-awscli/" \
      org.label-schema.usage="https://github.com/dweomer/dockerfiles-awscli/blob/master/README.md" \
      org.label-schema.vcs-url="https://github.com/dweomer/dockerfiles-awscli/" \
      org.label-schema.schema-version="1.0"
