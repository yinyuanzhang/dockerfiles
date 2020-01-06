FROM gliderlabs/alpine:3.4

RUN \
  apk --update add \
    sudo \
    ca-certificates \
    curl \
    openssh-client \
    openssl \
    python \
    py-pip \
    rsync \
    tar && \
  apk --update add --virtual build-dependencies \
    build-base \
    libffi-dev \
    openssl-dev \
    python-dev && \
  pip install --upgrade \
    ansible \
    cffi \
    pip \
    && \
  apk del build-dependencies && \
  rm -rf /var/cache/apk/*

RUN mkdir /etc/ansible/ /ansible
RUN echo "[local]" >> /etc/ansible/hosts && \
    echo "localhost" >> /etc/ansible/hosts

RUN mkdir -p /ansible/playbooks
WORKDIR /ansible/playbooks

ENV ANSIBLE_HOST_KEY_CHECKING false
ENV PATH /ansible/bin:$PATH
ENV PYTHONPATH /ansible/lib

ENTRYPOINT ["ansible-playbook"]
