FROM docker:stable

ARG ANSIBLE_VERSION=2.8.*

ENV ANSIBLE_VERSION=${ANSIBLE_VERSION}

LABEL maintainer="team@lean-delivery.com"

RUN apk add --no-cache git py-pip python-dev gcc musl-dev libffi-dev openssl-dev make
RUN apk add --no-cache openssh-client

RUN pip install --upgrade pip
RUN pip install git+git://github.com/ansible/molecule@2.22
RUN pip install --upgrade ansible==$ANSIBLE_VERSION docker pyOpenSSL PyYAML pytest
RUN pip install pywinrm[credssp] boto boto3
RUN pip install git+https://github.com/ansible/ansible-lint.git && \
    ansible --version && \
    ansible-lint --version && \
    molecule --version
