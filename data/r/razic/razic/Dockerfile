FROM ubuntu:latest

# packages
RUN apt-get update && \
    apt-get install -y \
    make \
    gcc \
    build-essential \
    locales \
    man \
    bash-completion \
    curl \
    git \
    mercurial

# locales
RUN locale-gen en_US.UTF-8

# env vars
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV HOME /root

# git completion
RUN cd /etc/bash_completion.d && \
    curl \
    -sLO \
    https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash

# config files
ADD .bash_profile /root/.bash_profile
ADD .gitconfig /root/.gitconfig

# share home directory
VOLUME /root

# enter home directory
WORKDIR /root

# enter bash
ENTRYPOINT ["bash", "-il"]
