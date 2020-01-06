FROM debian:jessie
MAINTAINER Stephen Tudor <studor@ebay.com>

ENV LANG=en_US.UTF-8 \
    TERM=xterm-256color

# install bin and lib dependencies
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    locales \
    build-essential \
    nodejs \
    npm \
    python-pygments \
    ruby-dev \
    ruby \
  && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
  && locale-gen \
  && rm -rf /var/lib/apt/lists/*

# install node dependencies
RUN ln -sf /usr/bin/nodejs /usr/bin/node \
  && npm update -g npm \
  && npm install -g grunt-cli

# install ruby dependencies
COPY .gemrc $HOME/.gemrc
RUN gem install \
    jekyll \
    rdiscount \
    compass

WORKDIR /src

CMD npm install && grunt
