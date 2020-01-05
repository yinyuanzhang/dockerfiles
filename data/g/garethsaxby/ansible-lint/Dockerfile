FROM library/alpine:3.8

ARG BUILD_VERSION=3.4.23
ENV VERSION=${BUILD_VERSION}

RUN apk --no-cache add python2 py2-pip python2-dev build-base py2-cffi openssl-dev && \
pip install ansible-lint==${VERSION} && \
apk --no-cache del python2-dev build-base openssl-dev

ENTRYPOINT [ "ansible-lint" ]