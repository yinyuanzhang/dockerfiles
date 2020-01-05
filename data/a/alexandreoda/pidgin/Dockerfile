FROM debian:stretch-slim

LABEL authors https://www.oda-alexandre.com/

ENV USER pidgin
ENV HOME /home/${USER}
ENV LOCALES fr_FR.UTF-8

RUN echo -e '\033[36;1m ******* INSTALL APP ******** \033[0m'; \
  apt-get update && apt-get install -y \
  locales \
  sudo \
  pidgin \
  pidgin-otr \
  tor \
  privoxy \
  libcanberra-gtk-module

RUN echo -e '\033[36;1m ******* CHANGE LOCALES ******** \033[0m'; \
  locale-gen ${LOCALES}
  
RUN echo -e '\033[36;1m ******* ADD USER ******** \033[0m'; \
  useradd -d ${HOME} -m ${USER}; \
  passwd -d ${USER}; \
  adduser ${USER} sudo

RUN echo -e '\033[36;1m ******* SELECT USER ******** \033[0m'
USER ${USER}

RUN echo -e '\033[36;1m ******* SELECT WORKING SPACE ******** \033[0m'
WORKDIR ${HOME}

RUN echo -e '\033[36;1m ******* CONFIG TOR & PRIVOXY ******** \033[0m'; \
  sudo rm -f /etc/privoxy/config; \
  sudo rm -f /etc/tor/torcc; \
  echo "listen-address localhost:8118" | sudo tee -a /etc/privoxy/config; \
  echo "forward-socks5 / localhost:9050 ." | sudo tee -a /etc/privoxy/config; \
  echo "forward-socks4 / localhost:9050 ." | sudo tee -a /etc/privoxy/config; \
  echo "forward-socks4a / localhost:9050 ." | sudo tee -a /etc/privoxy/config; \
  echo "SOCKSPort localhost:9050" | sudo tee -a /etc/tor/torcc

RUN echo -e '\033[36;1m ******* CLEANING ******** \033[0m'; \
  sudo apt-get --purge autoremove -y; \
  sudo apt-get autoclean -y; \
  sudo rm /etc/apt/sources.list; \
  sudo rm -rf /var/cache/apt/archives/*; \
  sudo rm -rf /var/lib/apt/lists/*

RUN echo -e '\033[36;1m ******* CONTAINER START COMMAND ******** \033[0m'
CMD sudo service tor start && sudo service privoxy start && pidgin -f \