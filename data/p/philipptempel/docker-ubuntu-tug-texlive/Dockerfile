FROM ubuntu:xenial

MAINTAINER Philipp Tempel <mail@philipptempel.me>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qy \
  && apt-get install -qy apt-utils \
  && apt-get upgrade -qy \
  && apt-get dist-upgrade -qy \
  && apt-get update -qy \
  && apt-get install -qy \
  curl \
  perl \
  wget \
  ghostscript \
  imagemagick \
  python-pygments \
  python3-pygments \
  git \
  gcc \
  make \
  musl \
  rsync \
  gnuplot

ADD texlive.profile /tmp/texlive/texlive.profile

RUN cd /tmp/ \
  && wget --user=anonymous --password=ftp --no-parent --no-verbose --recursive --no-host-directories --cut-dirs=4 ftp://tug.org/historic/systems/texlive/2016/tlnet-final/ \
  && cd /tmp/tlnet-final \
  && tar -xzf install-tl-unx.tar.gz \
  && cd install-tl-* \
  && ./install-tl -profile=/tmp/texlive/texlive.profile -repository /tmp/tlnet-final/ \
  && cd / \
  && rm -rf /tmp/tlnet-final/

ENV PATH="/usr/local/texlive/2016/bin/x86_64-linux/:$PATH" \
  MANPATH="/usr/local/texlive/2016/texmf-dist/doc/man:$MANPATH" \
  INFOPATH="/usr/local/texlive/2016/texmf-dist/doc/info:$INFOPATH"

RUN luaotfload-tool --cache=erase \
  && luaotfload-tool --force \
  && texhash
