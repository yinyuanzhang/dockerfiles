FROM linuxserver/deluge
MAINTAINER Jean Blanchard <jean@blanchard.io>

# Install sftp
RUN apt-get update \
  && apt-get install -y openssh-client \
  && rm -rf /var/lib/apt/lists/*
