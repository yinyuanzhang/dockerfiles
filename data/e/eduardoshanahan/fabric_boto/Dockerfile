FROM eduardoshanahan/fabric:1.14.0.5

LABEL maintainer 'Eduardo Shanahan <contact@eduardoshanahan.com>'

RUN apk add --virtual .install_dependencies_fabric_boto \
    py-pip \
&&  pip install boto3 \
&&  apk del .install_dependencies_fabric_boto

ENTRYPOINT ["/bin/sh"]
