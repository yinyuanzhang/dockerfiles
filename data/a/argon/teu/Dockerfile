FROM debian:buster
MAINTAINER Andrew Naylor <argon@mkbot.net>


RUN echo "===> Installing curl..."  && \
    apt-get update -y  &&  apt-get install --fix-missing          && \
    DEBIAN_FRONTEND=noninteractive         \
    apt-get install -y curl  && \
    \
    echo "===> Removing unused APT resources..."                  && \
    apt-get clean                                                 && \
    rm -rf /var/lib/apt/lists/*  /tmp/*


# default command: display Ansible version
CMD [ "bash" ]
