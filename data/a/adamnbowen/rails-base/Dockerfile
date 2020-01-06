FROM ruby:2.6.5-stretch

# Set timezone
RUN echo "America/Chicago" > /etc/timezone && \
  dpkg-reconfigure -f noninteractive tzdata

# General dependencies:
RUN apt-get update && \
  apt-get install -y \
  build-essential \
  --no-install-recommends && \
  rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y yarn

# Install Postgres client
RUN touch /etc/apt/sources.list.d/pgdg.list && \
  echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' \
  >> /etc/apt/sources.list.d/pgdg.list && \
  wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
  apt-get update && \
  apt-get install -y postgresql-client-10 \
  --no-install-recommends && \
  rm -rf /var/lib/apt/lists/*

# Install headless-chrome
RUN apt-get update \
  && apt-get -yf install \
  libxss1 \
  libappindicator1 \
  libindicator7 \
  gconf-service \
  libasound2 \
  libgconf-2-4 \
  libgtk-3-0 \
  libnspr4 \
  libx11-xcb1 \
  libxtst6 \
  fonts-liberation \
  libnss3 \
  lsb-release \
  xdg-utils \
  libappindicator3-1 \
  && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && dpkg -i google-chrome*.deb \
  && apt-get -yf install xvfb \
  && apt-get -yf install unzip \
  && wget -N http://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip \
  && unzip chromedriver_linux64.zip \
  && chmod +x chromedriver \
  && mv -f chromedriver /usr/local/share/chromedriver \
  && ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver \
  && ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

# Install heroku toolbelt
RUN curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
