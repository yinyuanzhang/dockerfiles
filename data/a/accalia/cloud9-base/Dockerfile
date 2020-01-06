FROM ubuntu

LABEL maintainer="docker@elementia.me"

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Add the user
RUN groupadd -g 1000 ubuntu \
  && \
  useradd --uid 1000 --shell /bin/bash -m --home-dir /home/ubuntu -g ubuntu -G sudo ubuntu \
  && \
  # Inflate the base image to include all files, useful for development
  rm /etc/dpkg/dpkg.cfg.d/excludes \
  && \
  apt-get update --fix-missing \
  && \
  echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections \
  && \
  dpkg -l | grep ^ii | cut -d' ' -f3 | xargs apt-get install -y --reinstall \
  && \
  apt-get -y dist-upgrade \
  && \
  # Install some development tools
  apt-get install -y \
    bash \
    bash-completion \
    build-essential \
    curl \
    dnsutils \
    fakeroot \
    git \
    iputils-ping \
    jq \
    man-db \
    nano \
    # needed for eslint_d
    netcat-openbsd \ 
    parallel \
    python \
    python3 \
    python3-pip \
    python3-virtualenv \
    sudo \
    postgresql-client-common \
    time \
    tmux \
    tree \
    wget \
    zip \
  && \
  chmod 777 /tmp \
  && \
  sed -i 's/%sudo\s.*/%sudo ALL=NOPASSWD:ALL/' /etc/sudoers 
  # install cloud9
ADD cloud9sdk.tar.bz2 /cloud9sdk
ADD cloud9.tar.bz2 /cloud9

RUN chown -R ubuntu:ubuntu /cloud9 /cloud9sdk \
  && \
  chmod -R ug+rwX /cloud9 /cloud9sdk \
  && \
  # Allow better sudo
  sed -i -e 's_127.0.0.1_0.0.0.0_g' /cloud9sdk/configs/standalone.js

EXPOSE 52924/tcp 8080/tcp 3000-3999/tcp 3000-3999/udp

VOLUME /home/ubuntu
VOLUME /data

USER ubuntu
CMD ["/cloud9/node/bin/node", "/cloud9sdk/server.js", "--listen", "0.0.0.0", "-a", ":", "--port", "52924", "-w", "/home/ubuntu"]

HEALTHCHECK CMD curl -f http://localhost:52924/ide.html >/dev/null
