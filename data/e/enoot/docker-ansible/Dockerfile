FROM alpine:3.9

MAINTAINER Igor Martynyuk <igor.martynyuk@nuweb.com>

RUN \
  echo "*** get the latest list of available packages ***" && \
  apk update && \
  echo "*** add python runtime ***" && \
  apk add --no-cache --upgrade \
        python3 \
        openssl \
        ca-certificates && \
  apk add --update --virtual build-dependencies \
        python3-dev \
        libffi-dev \
        openssl-dev \
        build-base && \
  pip3 install -U \
        pip \
        cffi && \
  echo "*** install Ansible ***" && \
  pip3 install -U \
        ansible && \
  echo "*** install handy tools ***" && \
  pip install -U \
        pycrypto \
        pywinrm \
        boto \
        boto3 \
        ansible-lint && \
  apk add --no-cache --upgrade \
        sshpass \
        openssh-client \
        rsync \
        git \
        grep \
        findutils && \
  echo "*** remove package list ***" && \
  echo "**** cleanup ****" && \
  apk del build-dependencies && \
  rm -rf \
    /tmp/* \
    /var/cache/apk/* && \
  echo "*** Adding hosts for convenience ***" && \
  mkdir -p /etc/ansible && \
  echo 'localhost' > /etc/ansible/hosts 

# default command: display Ansible version
CMD [ "ansible-playbook", "--version" ]
