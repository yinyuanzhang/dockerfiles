FROM debian:stretch-slim

LABEL authors https://www.oda-alexandre.com/

ENV USER chromium
ENV HOME /home/${USER}
ENV LOCALES fr_FR.UTF-8

RUN echo -e '\033[36;1m ******* INSTALL PACKAGES ******** \033[0m'; \
  apt update && apt install --no-install-recommends -y \
  sudo \
  locales \
  ca-certificates \
  x11-xserver-utils \
  dirmngr \
  alsa-utils \
  libasound2 \
  libasound2-plugins \
  pulseaudio \
  pulseaudio-utils \
  libcanberra-gtk-module \
  libgtk-3-0

RUN echo -e '\033[36;1m ******* CHANGE LOCALES ******** \033[0m'; \
  locale-gen ${LOCALES}

RUN echo -e '\033[36;1m ******* INSTALL APP ******** \033[0m'; \
  apt update && apt install -y \
  chromium \
  chromium-l10n \
  chromium-driver

RUN echo -e '\033[36;1m ******* ADD USER ******** \033[0m'; \
  useradd -d ${HOME} -m ${USER}; \
  passwd -d ${USER}; \
  adduser ${USER} sudo

RUN echo -e '\033[36;1m ******* SELECT USER ******** \033[0m'
USER ${USER}

RUN echo -e '\033[36;1m ******* SELECT WORKING SPACE ******** \033[0m'
WORKDIR ${HOME}

RUN echo -e '\033[36;1m ******* CLEANING ******** \033[0m'; \
  sudo apt-get --purge autoremove -y; \
  sudo apt-get autoclean -y; \
  sudo rm /etc/apt/sources.list; \
  sudo rm -rf /var/cache/apt/archives/*; \
  sudo rm -rf /var/lib/apt/lists/*
  
RUN echo -e '\033[36;1m ******* CONTAINER START COMMAND ******** \033[0m'
CMD chromium --temp-profile --no-sandbox \