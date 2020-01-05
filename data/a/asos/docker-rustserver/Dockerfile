FROM ubuntu:16.04

MAINTAINER ASoS Gaming

# Set correct environment variables.
ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root


RUN apt-get clean && apt-get update && apt-get install -y \
    locales \
    apt-utils \
    tzdata && locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN echo "America/New_York" > /etc/timezone && dpkg-reconfigure tzdata

# Run a quick apt-get update/upgrade
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y && apt-get autoremove -y

# Install dependencies, mainly for SteamCMD
RUN apt-get install -y \
    ca-certificates \
    software-properties-common \
    python-software-properties \
    lib32gcc1 \
    libstdc++6 \
    curl \
    php \
    php-curl \
    nano \
    wget \
    bsdtar \
    zip \
    unzip \
    nginx \
    build-essential \
    expect \
    libgdiplus

# Run as root
USER root

# Remove default nginx stuff
RUN rm -fr /usr/share/nginx/html/* && \
	rm -fr /etc/nginx/sites-available/* && \
	rm -fr /etc/nginx/sites-enabled/*

# Install webrcon (specific commit)
COPY nginx_rcon.conf /etc/nginx/nginx.conf
RUN curl -sL https://github.com/Facepunch/webrcon/archive/465a8a1631ca3a94ba7d7c9bc3db33001c5bd352.zip | bsdtar -xvf- -C /tmp && \
	mv /tmp/webrcon-465a8a1631ca3a94ba7d7c9bc3db33001c5bd352/* /usr/share/nginx/html/ && \
	rm -fr /tmp/webrcon-465a8a1631ca3a94ba7d7c9bc3db33001c5bd352

# Customize the webrcon package to fit our needs
ADD fix_conn.sh /tmp/fix_conn.sh

# Create and set the steamcmd folder as a volume
RUN mkdir -p /steamcmd/rust
VOLUME ["/steamcmd/rust"]

# Install NodeJS (see below)
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs

# Setup proper shutdown support
ADD shutdown_app/ /shutdown_app/
WORKDIR /shutdown_app
RUN npm install

# Setup restart support (for update automation)
ADD restart_app/ /restart_app/
WORKDIR /restart_app
RUN npm install

# Setup scheduling support
ADD scheduler_app/ /scheduler_app/
WORKDIR /scheduler_app
RUN npm install

# Setup rcon command relay app
ADD rcon_app/ /rcon_app/
WORKDIR /rcon_app
RUN npm install
RUN ln -s /rcon_app/app.js /usr/bin/rcon

# Add the steamcmd installation script
ADD install.txt /install.txt

# Copy the Rust startup script
ADD start_rust.sh /start.sh

# Copy the Rust update check script
ADD update_check.sh /update_check.sh

# Set the current working directory
WORKDIR /

# Expose necessary ports
EXPOSE 8080
EXPOSE 28015
EXPOSE 28016

# Setup default environment variables for the server
ENV RUST_SERVER_STARTUP_ARGUMENTS "-batchmode -load +server.secure 1"
ENV RUST_SERVER_IDENTITY "docker"
ENV RUST_SERVER_SEED "12345"
ENV RUST_SERVER_NAME "Rust Server [DOCKER]"
ENV RUST_SERVER_DESCRIPTION "This is a Rust server running inside a Docker container!"
ENV RUST_SERVER_URL "https://hub.docker.com/r/asosgaming/docker-rustserver/"
ENV RUST_SERVER_BANNER_URL ""
ENV RUST_RCON_WEB "1"
ENV RUST_RCON_PORT "28016"
ENV RUST_RCON_PASSWORD "docker"
ENV RUST_UPDATE_CHECKING "0"
ENV RUST_UPDATE_BRANCH "public"
ENV RUST_START_MODE "0"
ENV RUST_OXIDE_ENABLED "0"
ENV RUST_OXIDE_UPDATE_ON_BOOT "1"
ENV RUST_SERVER_WORLDSIZE "3500"
ENV RUST_SERVER_MAXPLAYERS "500"
ENV RUST_SERVER_SAVE_INTERVAL "600"

# Cleanup
ENV DEBIAN_FRONTEND newt

# Start the server
ENTRYPOINT ["./start.sh"]
