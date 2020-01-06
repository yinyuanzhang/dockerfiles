FROM node:6

LABEL Name=node Version=6


# Install dependencies
RUN rm -rf /usr/local/bin/yarn /opt/yarn-* && \
    wget -q -O - https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb http://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y \
      google-chrome-stable \
      graphicsmagick \
      imagemagick \
      rsync \
      yarn \
      zip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install: phantomjs
RUN rm -rf /tmp/phantomjs \
    && mkdir /tmp/phantomjs \
    && curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 | tar -xj --strip-components=1 -C /tmp/phantomjs \
    && cd /tmp/phantomjs \
    && mv bin/phantomjs /usr/local/bin

