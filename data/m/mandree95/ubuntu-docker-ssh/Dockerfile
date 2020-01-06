FROM ubuntu

# ------------------- #
# Docker image labels #
# ------------------- #
LABEL description="Docker image with preinstalled ssh-client" \
 vendor="Marcel Andree" \
 maintainer="marcel@andree.cloud"

# ---------- #
# SSH-Client #
# ---------- #
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get -q -y install openssh-client \
  && mkdir -p ~/.ssh \
  && echo "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config
