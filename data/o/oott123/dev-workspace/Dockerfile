FROM ubuntu:18.04

RUN adduser --gecos '' --disabled-password coder && \
  chsh coder -s /bin/zsh && \
  apt-get update && \
  apt-get install -y \
  locales sudo dumb-init \
  vim curl wget \
  dnsutils iputils-ping \
  build-essential libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev libffi-dev \
  zsh openssh-server && \
  echo "coder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/nopasswd && \
  rm -f /ect/ssh/ssh_host* && \
  locale-gen en_US.UTF-8 && \
  mkdir -p /run/sshd

ENV LC_ALL=en_US.UTF-8
VOLUME ["/home/coder"]

ENTRYPOINT ["dumb-init", "/usr/sbin/sshd"]
