FROM alpine:3.8
MAINTAINER Remo Wenger <remo.wenger@mimacom.com>

ENV ANSIBLE_VERSION 2.7.0

RUN \
  apk --update add sudo && \
  apk --update add python py-pip openssl ca-certificates git && \
  apk --update add --virtual build-dependencies python-dev libffi-dev openssl-dev build-base && \
  pip install --upgrade pip cffi && \
  pip install ansible==${ANSIBLE_VERSION} && \
  pip install --upgrade pywinrm && \
  apk --update add sshpass openssh-client rsync && \
  apk del build-dependencies && \
  rm -rf /var/cache/apk/* && \
  mkdir -p /etc/ansible && \
  echo 'localhost' > /etc/ansible/hosts

CMD [ "ansible-playbook", "--version" ]

