FROM debian:stretch-slim

RUN set -x \
    && apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y curl openssh-server

RUN mkdir /var/run/sshd; deluser www-data

RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh; chmod u-s $(which passwd); chmod u-s $(which chpasswd)

EXPOSE 22

ENTRYPOINT ["/entrypoint.sh"]