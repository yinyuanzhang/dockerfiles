FROM alpine:latest

RUN apk --no-cache update && \
    apk --no-cache add python py-pip py-setuptools ca-certificates curl groff less jq git openssh && \
    pip --no-cache-dir install awscli && \
    rm -rf /var/cache/apk/*