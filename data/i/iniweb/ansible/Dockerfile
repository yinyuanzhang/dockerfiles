FROM alpine:3.7

MAINTAINER Anton Kasperovich <anton.kaspiarovich@gmail.com>

ENV ANSIBLE_VERSION 2.5.2
ENV ANSIBLE_LINT_VERSION 3.4.21
ENV ANSIBLE_REVIEW_VERSION 0.13.4
ENV PyOpenSSL_VERSION 17.5.0

RUN apk --update add sudo \
    git \
    python \
    py-pip \
    openssl \
    openssh \
    ca-certificates

RUN addgroup ansible \
    && adduser -s /bin/sh -D -G ansible ansible

RUN apk --update add --virtual build-dependencies \
    build-base \
    wget \
    python-dev \
    libffi-dev \
    openssl-dev \
    && pip install -U pyOpenSSL==$PyOpenSSL_VERSION \
    && pip install -U ansible==$ANSIBLE_VERSION \
    && pip install -U ansible-lint==$ANSIBLE_LINT_VERSION \
    && pip install -U ansible-review==$ANSIBLE_REVIEW_VERSION \
    && apk del build-dependencies

RUN mkdir -p /etc/ansible \
    && echo 'localhost' > /etc/ansible/hosts \
    && mkdir /ansible \
    && chown -R ansible:ansible /etc/ansible /ansible

USER ansible
VOLUME /ansible
WORKDIR /ansible

CMD [ "ansible-playbook", "--help" ]
