#######################################################
# Base image with my common software and configuration
#######################################################
FROM ubuntu:15.10
MAINTAINER Brandon Holt <holt.bg@gmail.com>

RUN apt-get update && apt-get install -y \
  pkg-config \
  build-essential \
  libboost-dev \
  wget curl \
  make cmake ninja-build \
  git \
  bash-completion \
  man \
  openssl \
  vim \
  ruby-full python-dev python-pip \
  zsh \
  mysql-client libmysqlclient-dev \
  tmux \
  inetutils-ping \
  gawk \
  dnsutils

RUN pip install ipython &&\
    gem install bundler rmate pry mysql2 sequel open4 rugged awesome_print

# setup `zsh` as shell & install `oh-my-zsh`
# (from https://github.com/robbyrussell/oh-my-zsh/blob/master/tools/install.sh)
RUN chsh -s /usr/bin/zsh root
ADD oh-my-zsh-install.sh /oh-my-zsh-install.sh
RUN sh /oh-my-zsh-install.sh || true && rm /oh-my-zsh-install.sh

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN mkdir /setup
ADD . /setup
RUN cat /setup/profile.bash >> /root/.bashrc; \
    cat /setup/profile.zsh > /root/.zshrc; \
    cat /setup/gitconfig >> /root/.gitconfig; \
    rm -r /root/.oh-my-zsh/custom; \
    cp -r /setup/oh-my-zsh-custom /root/.oh-my-zsh/custom; \
    cp /setup/dircolorsrc /root/.dircolorsrc; \
    echo '🐳 ' > /root/.box-name

ENV SHELL /usr/bin/zsh

ENV LD_LIBRARY_PATH  $LD_LIBRARY_PATH:/usr/local/lib
ENV CC               gcc
ENV CXX              g++
ENV LD               g++

CMD ["/usr/bin/zsh"]
