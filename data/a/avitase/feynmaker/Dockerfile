FROM ubuntu:latest

ARG USERNAME=richy

ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

RUN apt-get update -yq && \
apt-get install -yq \
apt-utils ca-certificates

RUN apt-get install -yq locales && locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

RUN apt-get update -yq && \
apt-get install -yq apt-utils
RUN apt-get install -yq \
texlive \
feynmf \
texlive-latex-extra \
texlive-luatex \
texlive-metapost \
texlive-pictures \
texlive-pstricks \
texlive-science
RUN apt-get install -yq \
build-essential \
ghostscript
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /output && \
mkdir -p /input && \
chmod -R a+rwX /output/ && \
chmod -R a+rwX /input/

RUN useradd -ms /bin/bash ${USERNAME}
USER ${USERNAME}
WORKDIR /home/${USERNAME}

USER root
COPY lhcb-symbols-def.tex template.tex Makefile make.sh /home/${USERNAME}/
RUN chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}/
USER ${USERNAME}

VOLUME ["/input", "/output"]
