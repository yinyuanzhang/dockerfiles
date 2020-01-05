### Dockerfile --- spacemacs-docker dockerfile with Emacs snapshot
##
## Copyright (c) 2012-2018 Sylvain Benner & Contributors
##
## Author: Eugene "JAremko" Yaremenko <w3techplayground@gmail.com>
##
##
## This file is not part of GNU Emacs.
##
### License: GPLv3
##
## See spacemacs/layers/+distributions/spacemacs-docker/README.org

# FROM jare/emacs:latest
# FROM jare/emacs:emacs24
# Emacs snapshot
FROM jare/emacs:latest

MAINTAINER JAremko <w3techplaygound@gmail.com>

ENV UNAME="spacemacser" \
    UID="1000"

# Default fonts
ENV NNG_URL="https://github.com/google/fonts/raw/master/ofl/\
nanumgothic/NanumGothic-Regular.ttf" \
    SCP_URL="https://github.com/adobe-fonts/source-code-pro/\
archive/2.030R-ro/1.050R-it.tar.gz"
RUN apt-get update && apt-get install wget git mplayer clang-format wmctrl direnv libvterm-dev libtool-bin\
    && mkdir -p /usr/local/share/fonts \
    && wget -qO- "${SCP_URL}" | tar xz -C /usr/local/share/fonts \
    && wget -q "${NNG_URL}" -P /usr/local/share/fonts \
    && wget https://github.com/sharkdp/fd/releases/download/v7.3.0/fd_7.3.0_amd64.deb \
    && git clone https://github.com/ztlevi/doom-config ${UHOME}/.doom.d \
    && dpkg -i fd_7.3.0_amd64.deb \
    && rm -rf fd_7.3.0_amd64.deb \
    && fc-cache -fv \
    && git clone -b develop https://github.com/hlissner/doom-emacs ${UHOME}/.emacs.d \
    && apt-get purge wget \
    && rm -rf /tmp/* /var/lib/apt/lists/* /root/.cache/*

# UHOME is /home/emacs (from jare/emacs)
ADD . ${UHOME}/

# Init Spacemacs
#RUN cp ${UHOME}/.emacs.d/core/templates/.spacemacs.template ${UHOME}/ \
RUN y | mv ${UHOME}/init.el ${UHOME}/.doom.d/init.el \
    && y | mv ${UHOME}/+ui.el ${UHOME}/.doom.d/+ui.el \
    && asEnvUser emacs -batch -u ${UNAME} -kill \
    && asEnvUser emacs -batch -u ${UNAME} -kill \
    && chmod ug+rw -R ${UHOME} \
    &&  yes|asEnvUser ${UHOME}/.emacs.d/bin/doom quickstart


#RUN ln -s \
#    ${UHOME}/.emacs.d/layers/+distributions/spacemacs-docker/deps-install/run \
#    /usr/local/sbin/install-deps \
#    && chown root:root /usr/local/sbin/install-deps \
#    && chmod 770 /usr/local/sbin/install-deps
