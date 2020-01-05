# based on https://github.com/buildkite/docker-puppeteer
FROM node:10.12.0-slim

RUN  apt-get update \
     # See https://crbug.com/795759
     && apt-get install -yq libgconf-2-4 \
     # Install latest chrome dev package, which installs the necessary libs to
     # make the bundled version of Chromium that Puppeteer installs work.
     && apt-get install -y wget --no-install-recommends \
     && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
     && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
     && apt-get update \
     && apt-get install -y google-chrome-unstable --no-install-recommends \
     && apt-get install -y git \
     && rm -rf /var/lib/apt/lists/* \
     && curl https://cli-assets.heroku.com/install.sh | sh 

# Add package.json with Puppeteer under /node_modules so it's available system-wide
ADD package.json package-lock.json /

# Install Puppeteer and other Little Bird Backend deps
RUN npm i && npm i -g yarn cross-env jest

# Install sentry-cli
RUN curl -sL https://sentry.io/get-cli/ | bash

ENV PATH="${PATH}:/node_modules/.bin"

# Versions of local tools
RUN echo "node: $(node -v)"; \
    echo "npm: $(npm -v)"; \
    echo "yarn: $(yarn -v)"
