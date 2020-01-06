FROM alpine:3.7

ARG PKG_BUILD="py-pip"
ARG PKG_EXTRA="bash bind-tools ca-certificates curl jq less wget"

ARG AWS_CFN_PACKAGE_URL="https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-latest.tar.gz"

RUN set -x \
 && apk add --update --no-cache \
    python \
    py-setuptools \
    $PKG_BUILD \
    $PKG_EXTRA \
 && pip --no-cache-dir install $AWS_CFN_PACKAGE_URL \
 && apk del $PKG_BUILD \
 && ls -alF /usr/bin/cfn*

CMD ["/bin/bash"]

LABEL org.label-schema.name="dweomer/awscfn" \
      org.label-schema.description="AWS CloudFormation Helper Scripts on Alpine" \
      org.label-schema.url="https://github.com/dweomer/dockerfiles-awscfn/" \
      org.label-schema.usage="https://github.com/dweomer/dockerfiles-awscfn/blob/master/README.md" \
      org.label-schema.vcs-url="https://github.com/dweomer/dockerfiles-awscfn/" \
      org.label-schema.schema-version="1.0"
