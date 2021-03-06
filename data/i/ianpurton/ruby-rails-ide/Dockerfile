FROM ruby:2.5

RUN apt-get update -qq && apt-get install -y nodejs postgresql-client

RUN apt-get install -y curl \
   && curl https://cli-assets.heroku.com/install.sh | sh 

# Code-Server - Visual studio code dev env.
RUN apt-get update && apt-get install --no-install-recommends -y \
    bsdtar \
    openssl \
    locales \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

ENV CODE_VERSION="1.792-vsc1.33.1"
RUN curl -sL https://github.com/codercom/code-server/releases/download/${CODE_VERSION}/code-server${CODE_VERSION}-linux-x64.tar.gz | tar --strip-components=1 -zx -C /usr/local/bin code-server${CODE_VERSION}-linux-x64/code-server

# Postgres stuff.
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y && apt-get install -y --no-install-recommends postgresql postgresql-client

# Install chrome so we can have headless browser testing.
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get update \
    && dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install \
    && apt-get install -y fonts-liberation libappindicator1 xdg-utils \
    && apt-get install -y libnss3 

# Setup User
RUN groupadd -r coder \
    && useradd -m -r coder -g coder -s /bin/bash 
   # && echo "coder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/nopasswd
USER coder

RUN mkdir -p /home/coder/project

WORKDIR /home/coder/project

ENTRYPOINT ["code-server"]