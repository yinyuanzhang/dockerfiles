FROM ubuntu:latest

LABEL vendor="Guillaume Royer"

RUN set -x \
    && apt-get update \
    && apt-get install -y \
        curl \
        wget \
        gnupg \
        openssh-client \
        git

# Install node 8
RUN set -x \
    && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y \
        nodejs \
    && npm install -g npm@latest yarn@latest

# Install Chrome
RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/chrome.list
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN set -x \
    && apt-get update \
    && apt-get install -y \
        google-chrome-stable

ENV CHROME_BIN /usr/bin/google-chrome

# Install ruby
RUN set -x \
    && apt-get update \
    && apt-get install -y \
      ruby \
      ruby-dev \
      rubygems-integration

# Install haml
RUN gem install haml

# Install codeceptjs and webdrivers
RUN npm install -g codeceptjs protractor@5.3.1
RUN webdriver-manager update

# RUN node -v
# RUN npm -v
# RUN ruby -v
# RUN haml -v
