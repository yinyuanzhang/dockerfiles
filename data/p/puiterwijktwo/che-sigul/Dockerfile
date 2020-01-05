FROM codenvy/ubuntu_jre

RUN sudo apt-get update && \
  sudo apt-get install -y gcc make python-pip zlibc zlib1g zlib1g-dev libssl-dev libnss3-tools python-nss python-sqlalchemy

WORKDIR /projects
CMD tailf /dev/null
