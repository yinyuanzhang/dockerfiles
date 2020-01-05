FROM debian:stretch

LABEL version="1.0" \
      maintainer="igoticecream@gmail.com" \
      description="Docker image for Nintendo Switch homebrew development"

# Environment variables
ENV DEBIAN_FRONTEND     noninteractive
ENV HOME                /home/homebrew
ENV LIBTRANSISTOR_HOME  /opt/libtransistor/
ENV DEVKITPRO           /opt/devkitpro
ENV DEVKITARM           $DEVKITPRO/devkitARM
ENV DEVKITA64           $DEVKITPRO/devkitA64
ENV LIBNX               $DEVKITPRO/libnx
ENV PORTLIBS            $DEVKITPRO/portlibs/switch
ENV SWITCHTOOLS         $DEVKITPRO/tools
ENV PACMAN              $DEVKITPRO/pacman
ENV PATH                $PATH:$DEVKITARM/bin
ENV PATH                $PATH:$DEVKITA64/bin
ENV PATH                $PATH:$PORTLIBS/bin
ENV PATH                $PATH:$SWITCHTOOLS/bin
ENV PATH                $PATH:$PACMAN/bin

# Basic tools
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y apt-utils && \
    apt-get install -y build-essential && \
    apt-get install -y --no-install-recommends sudo ca-certificates pkg-config curl wget bzip2 xz-utils make git bsdtar doxygen gnupg unzip zip ssh cmake manpages-dev man-db && \
    apt-get clean -y

# Libtransistor
RUN curl -s https://api.github.com/repos/reswitched/libtransistor/releases/latest | \
    grep "browser_download.*libtransistor.*libtransistor.*zip" | \
    cut -d : -f 2,3 | \
    tr -d '"' | \
    xargs -I {} curl -fSL --output /var/tmp/libtransistor.zip {} && \
    unzip /var/tmp/libtransistor.zip -d $LIBTRANSISTOR_HOME

# Devkitpro
RUN wget https://github.com/devkitPro/pacman/releases/download/devkitpro-pacman-1.0.1/devkitpro-pacman.deb && \
    dpkg -i devkitpro-pacman.deb && \
    rm devkitpro-pacman.deb && \
    dkp-pacman -Syyu --noconfirm switch-dev && \
    dkp-pacman -S --needed --noconfirm `dkp-pacman -Slq dkp-libs | grep '^switch-'` && \
    dkp-pacman -Sy --noconfirm devkitARM && \
    dkp-pacman -Scc --noconfirm

# Custom scripts
RUN echo -e '#!/bin/bash\ndkp-pacman -Syyu --noconfirm && dkp-pacman -Scc --noconfirm' > /usr/local/bin/update && \
    chmod +x /usr/local/bin/update

VOLUME  /homebrew
WORKDIR /homebrew
