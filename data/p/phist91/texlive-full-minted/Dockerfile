# Dockerfile for a Docker image providing a full up-to-date TeX Live
# installation with minted package support (and therefore with Python and
# Pygments).
# Build may fail at times because of CTAN choosing a broken mirror.

FROM debian:latest
LABEL maintainer="p.st@wwu.de"
COPY texlive-full-minted/texlive.profile /
ARG TLSETUP_PATH=http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
# Basic system and Python / Pygments setup
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y \
        wget \
        perl \
        fontconfig \
        libwww-perl \
        python3 \
        python3-pip \
        ghostscript \
    && pip3 install Pygments \
    && rm -rf /var/lib/apt/lists/*
	
# Installing TeX Live
RUN wget $TLSETUP_PATH \
    && tar xzvf install-tl-unx.tar.gz \
    && ./install-tl-*/install-tl -profile /texlive.profile \
    && rm -rf install-tl-*
