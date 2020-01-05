FROM elixir:slim

# install basic utilities
RUN echo "deb http://ftp.us.debian.org/debian testing main contrib non-free" >> /etc/apt/sources.list &&\
        apt-get update &&\
        apt-get install -y \
                curl \
                shellcheck \
                inotify-tools \
                gnupg \
                git \
                nano

# install node.js
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash - \
 && apt-get install -y nodejs

# install yarn & webpack
RUN npm install -g \
        yarn \
        webpack \ 
        webpack-cli

# cleanup after package installs
RUN apt-get purge -y --auto-remove \
        curl \
        gnupg \
 && rm -rf /var/lib/apt/lists/*

# install the phoenix mix archive
RUN mix local.hex --force &&\
    mix local.rebar --force &&\
    mix archive.install --force https://github.com/phoenixframework/archives/raw/master/phx_new.ez

WORKDIR /app