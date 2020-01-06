FROM quay.io/pterodactyl/core:java

USER root

RUN apt-get update; \
        apt-get install -y --no-install-recommends wget curl iputils-ping sudo; \
        apt-get upgrade -y; \
        apt-get purge -y --auto-remove

RUN useradd -u 999 -d /home/container -m pterodactyl; \
        adduser pterodactyl sudo; \
        echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers; \
        usermod pterodactyl -g 0; \
        echo usermod pterodactyl -ou 0 -g 0

CMD ["/bin/bash", "/entrypoint.sh"]