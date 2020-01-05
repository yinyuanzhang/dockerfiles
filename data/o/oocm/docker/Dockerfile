# EggShell
# iOS/macOS Remote Administration Tool
# https://github.com/neoneggplant/EggShell
# docker build -t eggshell .
FROM ubuntu:16.04

RUN \
  apt update && \
  apt install -y python-pip git-core && \
  pip install pycrypto && \
  cd /opt && \
  git clone https://github.com/neoneggplant/EggShell

COPY start.sh /start.sh

RUN \
  apt remove -y git-core && \
  apt clean && \
  apt autoremove -y && \
  chmod 775 /start.sh

EXPOSE 4444

ENTRYPOINT ["/start.sh"]
