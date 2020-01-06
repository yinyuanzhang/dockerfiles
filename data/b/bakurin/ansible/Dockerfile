FROM alpine:3.7

RUN apk --update --no-cache add ansible openssh-client rsync sshpass py-netaddr && \
    rm -rf /var/cache/apk/* && \
    mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts

WORKDIR /ansible

COPY ansible.cfg ansible.cfg
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

VOLUME /ansible/playbook

ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["--version"]