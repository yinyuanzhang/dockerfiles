FROM python:3.7.2-alpine3.9

ENV ANSIBLE_LINT_VERSION=4.1.0

RUN apk add --no-cache --virtual .build-deps \
      make \
      gcc \
      libffi-dev \
      linux-headers \
      musl-dev \
      openssl-dev && \
\
    pip install ansible-lint==$ANSIBLE_LINT_VERSION && \
\
    runDeps="$( \
      scanelf --needed --nobanner --format '%n#p' --recursive /usr/local/lib \
      | tr ',' '\n' \
      | sort -u \
      | awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }' \
      )" && \
    apk add --virtual .run-deps $runDeps && \
    apk del .build-deps

CMD ["/usr/local/bin/ansible-lint", "--help"]

LABEL org.label-schema.schema-version="1.0" \
      org.label-schema.name="ansible-lint" \
      org.label-schema.version="4.1.0" \
      org.label-schema.url="https://github.com/willthames/ansible-lint" \
      org.label-schema.vcs-url="https://github.com/oildex/docker-ansible-lint"
