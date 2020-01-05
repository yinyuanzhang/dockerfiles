FROM node:alpine

LABEL \
    version="1.0" \
    maintainer="José Luis Salvador Rufo <salvador.joseluis@gmail.com>"

RUN apk add --no-cache git curl jq openssh-client python g++ make py2-pip \
    && pip install awscli \
    && sed -i '/set -e/a\\n[ ! -z "$DEBUG" ] && set -x' /usr/local/bin/docker-entrypoint.sh \
    && sed -i '/set -e/a\\n[ -d /docker-entrypoint.d ] && for f in /docker-entrypoint.d/*; do\n\tif [ -x "$f" ]; then\n\t\techo "$0: running $f"\n\t\t"$f"\n\telse\n\t\techo "$0: ignoring $f"\n\tfi\ndone' /usr/local/bin/docker-entrypoint.sh \
    && sed -i '/set -e/a\\n[ ! -z "$ARTIFACT_S3" ] && mkdir -p /app && aws s3 cp "$ARTIFACT_S3" - | tar zx -C /app/' /usr/local/bin/docker-entrypoint.sh
