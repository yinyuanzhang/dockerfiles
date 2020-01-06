FROM janitortechnology/ubuntu-dev
MAINTAINER Etienne Wan "etiennewan@defora.org"

USER root
RUN mkdir -p /var/lib/apt/lists/partial && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  pkg-config \
  libxml2-utils \
  xsltproc \
  glib2.0 \
  gtk-doc-tools

RUN chgrp -R staff /usr/local \
  && chmod -R g+ws /usr/local \
  && adduser user staff

USER user
RUN git clone https://github.com/DeforaOS/DeforaOS.git \
 && cd DeforaOS

WORKDIR /home/user/DeforaOS

ENV WORKSPACE /home/user/DeforaOS
