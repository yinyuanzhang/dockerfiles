FROM alpine:latest

RUN apk add --no-cache \
    bind-tools \
    bash \
    curl \
    jq \
    mongodb \
    mongodb-tools \
    mysql-client \
    openssh-client \
    python3

RUN curl -L -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.11.0/bin/linux/amd64/kubectl && chmod +x /usr/bin/kubectl

RUN python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN apk --no-cache add --virtual=build gcc libffi-dev musl-dev openssl-dev python-dev python3-dev make && \
    pip install awscli s3cmd azure-cli && \
    apk del --purge build
