FROM alpine:3.8

ENV PATH /root/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

COPY ssh-env-config.sh /usr/bin/
COPY ssh_config /root/.ssh/config

RUN apk update && \
    apk add --no-cache --update \
      openssh-client \
      rsync \
      curl \
      git \
      python3 \
      py3-pip \
      bash && \
    ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime && \
    apk add --no-cache --update \
      --virtual .build-deps \
      groff \
      python3-dev \
      libffi-dev \
      openssl-dev \
      build-base && \
    pip3 install --upgrade pip cffi && \
    pip3 install \
      awscli \
      ansible && \
    mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts && \
    apk del --purge -v \
      python3-dev \
      libffi-dev \
      openssl-dev \
      build-base && \
    apk del .build-deps && \
    rm /var/cache/apk/* && \
    chmod +x /usr/bin/ssh-env-config.sh

ENTRYPOINT ["ssh-env-config.sh"]

CMD ["/bin/bash"]
