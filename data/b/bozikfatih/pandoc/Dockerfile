FROM ubuntu:trusty

MAINTAINER Fatih Bozik <bozikfatih@gmail.com>

# Install Latex
RUN apt-get update && apt-get install -y \
    texlive-full \
    wget \
 && rm -rf /var/lib/apt/lists/*

ENV PKGREL 1
ENV VERSION 2.1.3

# Install pandoc
ADD https://github.com/jgm/pandoc/releases/download/${VERSION}/pandoc-${VERSION}-${PKGREL}-amd64.deb /pandoc.deb
RUN dpkg --install pandoc.deb && \
    rm -rf pandoc.deb

RUN mkdir -p /source

# Define mountable directories
VOLUME ["/source", "/usr/local/share/fonts"]

# Define working directory
WORKDIR /source

ENTRYPOINT ["pandoc"]
