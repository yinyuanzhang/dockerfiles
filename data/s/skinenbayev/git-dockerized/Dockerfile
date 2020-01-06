FROM ubuntu:16.04

RUN apt-get update && apt-get install -y git openssh-server locales

COPY --chown=root:root sshd_config /etc/ssh/sshd_config

RUN locale-gen en_US.UTF-8 \
    && mkdir /var/run/sshd \
    && adduser --disabled-password --gecos "" git \
    && cd /home/git \
    && mkdir .ssh/ && chmod 700 .ssh \
    && touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys \
    && mkdir repos \
    && git init --bare repos/helloworld \
    && chown -R git:git .ssh/ \
    && chown -R git:git repos \
    && echo $(which git-shell) >> /etc/shells \
    && chsh git -s $(which git-shell)

EXPOSE 22

CMD ["/bin/bash", "-c", "cat /run/secrets/* > /home/git/.ssh/authorized_keys; /usr/sbin/sshd -D"]
