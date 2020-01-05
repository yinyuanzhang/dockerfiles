FROM python:3.8-alpine3.10

LABEL maintainer='Geoffrey Roguelon'

ARG AWS_CLI_VERSION="1.16.293"

ENV PIP_DISABLE_PIP_VERSION_CHECK true

RUN apk add --no-cache groff jq && \
  pip install awscli==${AWS_CLI_VERSION} && \
  mkdir -p "${HOME}/.aws"

ENTRYPOINT ["aws"]

CMD ["help"]
