FROM python:3.6.4-alpine3.7

ENV ANSIBLE_VERSION 2.4.3.0

RUN apk update && \
    apk add g++ \
            make \
            libffi-dev \
            openssl-dev \
            ca-certificates

RUN pip install ansible==$ANSIBLE_VERSION cryptography

ENTRYPOINT ["ansible-playbook"]
