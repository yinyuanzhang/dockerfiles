FROM alpine:3.8
MAINTAINER oudemen <oudemen@msn.com>
ARG ANSIBLE_VERSION=2.9.0
LABEL org.label-schema.version=${ANSIBLE_VERSION}
RUN apk --update --no-cache add ca-certificates python3  openssh-client sshpass openssl  git rsync && \
    apk --update add --virtual .build-dev python3-dev libffi-dev openssl-dev build-base && \
    pip3 install --upgrade pip cffi && \
    pip3 install ansible==${ANSIBLE_VERSION} && \
    apk del .build-dev && \
    rm -rf /var/cache/apk/* && \
    mkdir -p /etc/ansible 
CMD [ "ansible-playbook", "--version" ]
