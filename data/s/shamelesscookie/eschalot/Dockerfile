FROM ubuntu:18.04

RUN \
  apt update && \
  apt upgrade -y && \
  apt install -y git build-essential libssl-dev openssl && \
  git clone https://github.com/ReclaimYourPrivacy/eschalot.git && \
  mkdir -p /usr/lib/eschalot && \
  cd /eschalot && \
  make clean && \
  make && \
  cp eschalot /usr/bin && \
  cp worgen /usr/bin && \
  cp *.txt /usr/lib/eschalot && \
  cd / && \
  rm -rf /eschalot && \
  apt remove git build-essential libssl-dev -y && \
  apt-get autoremove -y && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

ENTRYPOINT	["eschalot"]