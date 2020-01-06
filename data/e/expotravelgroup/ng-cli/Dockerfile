FROM trion/ng-cli

ARG SSH_DIR="/etc/ssh"
ARG SSH_CONFIG="/etc/ssh/config"

USER root

RUN set -xe \
    && mkdir -p $SSH_DIR \
	&& echo -e "Host *\n\tStrictHostKeyChecking=no\n\n" > $SSH_CONFIG

RUN apt-get update && apt-get install -qqy openssh-client sshpass
