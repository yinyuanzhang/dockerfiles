FROM ubuntu:bionic

MAINTAINER Matthew Feickert <matthew.feickert@cern.ch>

WORKDIR /root

SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND noninteractive

# Install general dependencies
RUN apt-get -qq -y update && \
    apt-get -qq -y install \
        curl \
        wget \
        rsync \
        build-essential \
        zip \
        jq \
        git \
        libfontconfig \
        locales \
        software-properties-common \
        sshpass \
        ghostscript \
        vim \
        sudo && \
    apt-get -y autoclean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

# Download and install the latest TeX Live distribution using the texlive.profile from the repo
# http://tug.org/texlive/doc/texlive-en/texlive-en.html#x1-140003
COPY texlive.profile texlive.profile
RUN wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && \
    tar -zxvf install-tl-unx.tar.gz && \
    install-*/install-tl --profile=texlive.profile && \
    rm -rf /root/*

# Export useful TeX Live paths
ENV PATH /opt/texbin:$PATH
ENV PATH /usr/local/texlive/2018/bin/x86_64-linux:$PATH
ENV MAPATH /usr/local/texlive/2018/texmf-dist/doc/man:$MANPATH
ENV INFOPATH /usr/local/texlive/2018/texmf-dist/doc/info:$INFOPATH

# Generate font names database (and test latex along the way)
# http://tug.org/texlive/doc/texlive-en/texlive-en.html#x1-380003.5
RUN wget ftp://www.ctan.org/tex-archive/macros/latex/base/small2e.tex && \
    latex small2e.tex && \
    xelatex small2e.tex && \
    lualatex small2e.tex && \
    rm -rf /root/*

# Create user "docker" with sudo powers
RUN useradd -m docker && \
    usermod -aG sudo docker && \
    echo '%sudo ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers && \
    cp /root/.bashrc /home/docker/

WORKDIR /home/docker
ENV HOME /home/docker
ENV USER docker
USER docker
# Avoid first use of sudo warning. c.f. https://askubuntu.com/a/22614/781671
RUN touch $HOME/.sudo_as_admin_successful
CMD if [[ -f Makefile ]]; then make; else latex --version; fi && /bin/bash
