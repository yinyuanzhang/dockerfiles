FROM ubuntu:18.04

# Install base deps
RUN apt-get update && \
  apt-get install -y build-essential curl wget cmake python

# Install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb || true
RUN apt-get -y -f install
RUN rm google-chrome-stable_current_amd64.deb

# Install node
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y git nodejs wget && \
  rm -rf /var/lib/apt/lists/*
