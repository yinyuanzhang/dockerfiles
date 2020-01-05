FROM ruby:2.4.3-slim-stretch

ENV LC_ALL=C.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8

RUN printf "Acquire::http::Pipeline-Depth 0;\n\
  Acquire::http::No-Cache true;\n\
  Acquire::BrokenProxy true;" > /etc/apt/apt.conf.d/99fixbadproxy

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  curl \
  file \
  git \
  gnupg2 \
  imagemagick \
  libicu-dev \
  libmagickwand-dev \
  default-libmysqlclient-dev \
  libsqlite3-dev \
  libssl-dev \
  libxslt-dev \
  libxtst6 \
  libnss3 \
  libx11-xcb1 \
  libxss1 \
  libasound2 \
  libatk-bridge2.0-0 \
  libgtk-3-0 \
  mysql-client \
  openssh-client \
  python-dev \
  unzip \
  vim \
  zlib1g-dev \
  less \
  && rm -rf /var/lib/apt/lists/*

# Install latest chrome dev package and fonts to support major charsets (Chinese, Japanese, Arabic, Hebrew, Thai and a few others)
# Note: this installs the necessary libs to make the bundled version of Chromium that Puppeteer
# installs, work.
RUN curl -q -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
  && apt-get update \
  && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst ttf-freefont \
  --no-install-recommends \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /src/*.deb

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
  apt-get install -y --no-install-recommends nodejs && \
  npm install -g yarn && \
  rm -rf /var/lib/apt/lists/* && apt-get clean
