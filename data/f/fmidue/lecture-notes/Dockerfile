FROM ubuntu:bionic

LABEL Description="Image for building lecture notes (texlive + rail + fig2dev + gnuplot)" Vendor="Marcellus Siegburg" Version="1.0"

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      $(apt-cache depends texlive-full | grep Depends | grep -v '\-doc$' | sed 's/Depends://g') \
      fig2dev \
      wget \
      xzdec \
      make \
      gcc \
      libc-dev \
      bison \
      flex \
      gnuplot \
      unzip
WORKDIR /tmp
RUN wget http://mirrors.ctan.org/support/rail.zip \
 && unzip rail \
 && cd rail \
 && mkdir -p /usr/share/texmf/doc/man/manl \
 && sed -i "s#TEXDIR=\$(HOME)/tex#TEXDIR=/usr/share/texmf/tex/latex/rail#;s#BINDIR=\$(HOME)/bin#BINDIR=/usr/local/bin#;s#MANDIR=\$(HOME)/man#MANDIR=/usr/share/texmf/doc/man#" Makefile \
 && make install \
 && cd / && rm -rf /tmp/rail* \
 && apt-get remove -y gcc libc-dev bison flex unzip \
 && tlmgr init-usertree \
 && mkdir /work

WORKDIR /work
