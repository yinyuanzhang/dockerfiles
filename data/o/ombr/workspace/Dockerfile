FROM ubuntu:latest
MAINTAINER Luc Boissaye <luc@boissaye.fr>


RUN apt-get update -qq && \
  apt-get install -y -q --no-install-recommends \
    vim \
    tmux \
    screen \
    zsh \
    git \
    curl \
    sudo \
  && rm -rf /var/lib/apt/lists/* \
  && truncate -s 0 /var/log/*log

ENV ZDOTDIR=/dotfiles
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git /oh-my-zsh
ADD . /dotfiles

WORKDIR /home/u

RUN adduser --gecos '' --shell /bin/zsh u && passwd -d u && adduser u sudo
USER u

# RUN sudo apt-get update -qq

CMD /bin/zsh
