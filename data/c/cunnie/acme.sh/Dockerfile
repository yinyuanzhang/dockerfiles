FROM fedora

MAINTAINER Brian Cunnie <bcunnie@pivotal.io>

RUN dnf install -y git neovim python3-neovim bind-utils

RUN git clone https://github.com/neilpang/acme.sh

# Install Google and AWS CLI tools
RUN curl -OL https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-267.0.0-linux-x86_64.tar.gz; \
  tar xf *.gz; \
  /google-cloud-sdk/install.sh; \
  echo ". /google-cloud-sdk/path.bash.inc" >> /etc/bashrc; \
  rm *.gz
RUN pip3 install awscli --upgrade
