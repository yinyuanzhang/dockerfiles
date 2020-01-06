FROM debian:stretch-slim

MAINTAINER Pavel Argentov (argentoff@gmail.com)

# preparations
ENV DEBIAN_FRONTEND=noninteractive \
    TERM=linux

RUN sed -i 's/^mesg n$/tty -s \&\& mesg n/g' /root/.profile \
    && echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# apt preparations
RUN apt-get update \
    && apt-get dist-upgrade -y -q \
    && apt-get install -y -q \
       build-essential \
       apt-utils \
       wget \
       curl \
       make \
       git \
       m4 \
       unzip \
    && apt-get autoremove -y \
    && apt-get clean -y all \
    && rm -rf /var/lib/apt/lists/*

# locale
RUN apt-get update \
&& apt-get install -y -q \
locales \
tzdata \
&& apt-get autoremove -y \
&& apt-get clean -y all \
&& rm -rf /var/lib/apt/lists/*
RUN touch /usr/share/locale/locale.alias && \
localedef -i ru_RU -c -f UTF-8 -A /usr/share/locale/locale.alias ru_RU.UTF-8
ENV LANG=ru_RU.UTF-8 \
LANGUAGE=ru_RU:UTF-8 \
LC_ALL=ru_RU.UTF-8

# TZ
ENV SYSTEM_TIMEZONE=Europe/Moscow
RUN echo ${SYSTEM_TIMEZONE} > /etc/timezone \
&& cp /usr/share/zoneinfo/${SYSTEM_TIMEZONE} /etc/localtime \
&& dpkg-reconfigure -f noninteractive tzdata

# ocaml, opam et al.
WORKDIR /tmp
ENV VERSION=2.0.0-rc4
ENV ARCH=x86_64
ENV DISTFILE=opam-${VERSION}-${ARCH}-linux
RUN wget -nv https://github.com/ocaml/opam/releases/download/${VERSION}/${DISTFILE} && \
    install ${DISTFILE} /usr/local/bin/opam && \
    chmod a+x /usr/local/bin/opam && \
    rm -f ${DISTFILE}

# go out of setup mode
RUN echo 'debconf debconf/frontend select Dialog' | debconf-set-selections

# utop et al
RUN useradd -m -s /bin/bash dev
USER dev
WORKDIR /home/dev

RUN opam init -a --disable-sandboxing \
    && eval $(opam env) \
    && opam clean
RUN eval $(opam env) \
    && opam install -y utop \
    && opam clean

# entrypoint
ENTRYPOINT ["opam", "config", "exec", "--"]
CMD ["utop"]
