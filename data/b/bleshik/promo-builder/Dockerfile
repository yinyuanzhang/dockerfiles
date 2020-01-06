FROM ubuntu:18.04
COPY ./ /src
RUN apt-get update -y && apt-get install -y openssh-client npm python-pip python3-pip python3 wget curl default-jdk git ruby-full build-essential zlib1g-dev
RUN pip install awscli
RUN npm install -g n && n 8.10.0 && n use 8.10.0
RUN npm install npm@6.9.0 -g
RUN npm install -g yarn@1.3.2
RUN gem install jekyll bundler
