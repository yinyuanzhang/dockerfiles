FROM ubuntu:14.04

LABEL maintainer="Guys <guyschaos@gmail.com>"

# Install.
RUN \
  apt-get update && \
  # apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y asciidoc binutils uuid-runtime \
    bzip2 gawk gettext git libncurses5-dev \
    libz-dev patch unzip zlib1g-dev lib32gcc1 \
    libc6-dev-i386 subversion flex uglifyjs \
    git-core gcc-multilib p7zip p7zip-full msmtp \
    libssl-dev texinfo libglib2.0-dev xmlto qemu-utils \
    upx libelf-dev autoconf automake libtool autopoint wget curl && \
  rm -rf /var/lib/apt/lists/*

ARG UNAME=ledebuilder
ARG UID=1026
ARG GID=100
RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME
USER $UNAME
CMD ["bash"]
