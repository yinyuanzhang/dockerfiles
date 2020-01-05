FROM ubuntu:14.04

# Python, Git, Mercurial, Ruby, Curl
RUN apt-get update && apt-get install -y \
    python2.7 \
    python2.7-dev \
    python-pip \
    python-psycopg2 \
    libpq-dev \
    libxml2-dev \
    libxslt-dev \
    git \
    mercurial \
    ruby \
    curl

# Virtualenv deps - pycurl not working yet
RUN pip install virtualenv wheel chardet # pycurl

# Node
RUN curl -sL https://deb.nodesource.com/setup | sudo bash - && sudo apt-get install -y nodejs

# Grunt, Bower
RUN npm update -g npm && npm install -g grunt-cli && npm install -g bower