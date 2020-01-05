FROM debian:stable-slim

# Install nodejs
ENV NPM_CONFIG_LOGLEVEL=info NODE_VERSION=8

RUN apt-get update \
      # Install initially needed tools for setup
      && apt-get install -y -q --no-install-recommends \
        git \
        apt-transport-https \
        make \
        ca-certificates \
        gnupg \
        curl \
        fontconfig \
        ttf-freefont \

  # add yarn and node repos
  && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list \
  && echo 'deb https://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -y \
  
  # install node
  && curl -sL "https://deb.nodesource.com/setup_${NODE_VERSION}.x" | bash - \
  && apt-get install nodejs -yqq \

  # install chrome
  && apt-get -qqy --no-install-recommends install google-chrome-stable \

  # install yarn
  && apt-get install yarn \

  # some clean up before finishing this layer
  && rm -rf /var/lib/apt/lists/* \
  && apt-get clean
