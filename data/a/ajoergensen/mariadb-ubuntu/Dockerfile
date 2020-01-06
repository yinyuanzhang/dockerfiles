# vim:set ft=dockerfile:
FROM mariadb:10.4

ARG PKGS="ansible python-apt aptitude"
COPY install.yml packages.yml /

RUN \
        echo -e '#!/bin/bash\nexit 0' > /sbin/systemctl && \
        chmod +x /sbin/systemctl && \
        apt-get update && \
        apt-get -y install $PKGS && \
        ansible-playbook -D /install.yml && \
        apt-get -y purge $PKGS && \
        apt-get -y --purge autoremove && \
        apt-get -y clean && \
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /*.yml
