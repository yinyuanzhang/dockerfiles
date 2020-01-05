FROM alpine:3.7
LABEL maintainer="daryl.n.w.k@gmail.com"

RUN apk --update --no-cache add \
    python \
    py-pip \
    jq \
    openssh-client \
    && pip install --no-cache-dir awscli==1.16.138 \
    && apk del py-pip \
    && rm -rf /var/cache/apk/* /root/.cache/pip/*