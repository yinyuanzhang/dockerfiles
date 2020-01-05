FROM python:alpine

ARG AWS_SAM_CLI_VERSION
ENV AWS_SAM_CLI_VERSION ${AWS_SAM_CLI_VERSION:-0.23.0}

RUN set -ex; \
  apk add --no-cache gcc musl-dev; \
  pip --no-cache-dir install awscli aws-sam-cli==${AWS_SAM_CLI_VERSION}; \
  apk del gcc musl-dev

ENTRYPOINT ["sam"]
