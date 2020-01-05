# From LTS
FROM ubuntu:18.04

MAINTAINER https://fairen.github.io

# Installing dependencies
# Git
# Zsh
# Build-essential (make, gcc ..)
# Automake
# pkg-config
# libncurses5-dev libncursesw5-dev
RUN apt-get update
RUN apt-get install -y git zsh build-essential automake pkg-config libncurses5-dev libncursesw5-dev

# Install Tig
RUN git clone https://github.com/jonas/tig.git ${HOME}/tig &&\ 
  cd ${HOME}/tig &&\ 
  make clean &&\
  make configure &&\
  ./configure &&\
  make &&\ 
  make install

# Install fasd
RUN \
  git clone https://github.com/clvv/fasd.git /usr/local/fasd &&\ 
  ln -s /usr/local/fasd/fasd /usr/bin/fasd

# Installing Oh My ZSH
ENV ZSH ${HOME}/.oh-my-zsh
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ${HOME}/.oh-my-zsh
ADD home/ ${HOME}/
RUN chown -R ${uid}:${gid} ${HOME}

# Creating directory
RUN mkdir -p /home/workstation/Projects

# Define default command.
CMD ["zsh"]
