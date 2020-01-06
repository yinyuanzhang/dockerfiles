FROM ubuntu:18.04

WORKDIR /app

# echo shortcut for listing files
RUN echo 'alias ll="ls -lh"' >> ~/.bashrc
# update & upgrade
RUN apt-get update && apt-get upgrade -y
# install basics
RUN apt-get install -y \
  screen \
  openssl \
  nano \
  vim \
  zip \
  iputils-ping \
  unzip \
  git \
  telnet \
  software-properties-common \
  curl \
  ca-certificates \
  net-tools \
  wget \
  build-essential 

# install nodejs 10.x
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install nodejs -y
# Other nodejs modles
RUN npm install express-generator -g

# Install Go
RUN wget -c https://dl.google.com/go/go1.12.1.linux-amd64.tar.gz && \
  tar -C /usr/local -xzf go1.12.1.linux-amd64.tar.gz && \
  rm go1.12.1.linux-amd64.tar.gz && \
  echo "export PATH=\$PATH:/usr/local/go/bin" >> ~/.bashrc

# Set go workdir
RUN echo "export GOPATH=/app/go" >> ~/.bashrc

#EXPOSE 3000 80 443 1337 8080
