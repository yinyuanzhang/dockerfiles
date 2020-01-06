FROM debian:jessie

ARG NODE_SASS_BINDING_VERSION=linux-x64-51
RUN \
       cd /tmp/ \
    && apt-get update \
    && apt-get -y --no-install-recommends install \
        apt-transport-https \
        curl \
        ca-certificates \
        git \
        openssh-client \
        python \
        build-essential \
    && curl -sL https://deb.nodesource.com/setup_8.x | bash \
    && apt-get -y --no-install-recommends install nodejs \
    && apt-get -y --no-install-recommends install fontforge ttfautohint \
    && apt-get install -yq libgconf-2-4 \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get -y install yarn \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* /var/log/apt/* /var/log/*.log

# Use this sassc binary for the node-sass builds for faster building times
ENV SASS_BINARY_PATH=/opt/cache/${NODE_SASS_BINDING_VERSION}_binding.node

# Cache the node-sass binary
RUN \
    mkdir -p /opt/cache/ \
    && cd /opt/cache/ \
    && curl -L -O https://github.com/sass/node-sass/releases/download/v4.1.0/${NODE_SASS_BINDING_VERSION}_binding.node \
    && chmod +x $SASS_BINARY_PATH

## REGRESSION CSS ##

# Required for Regression Testing
RUN apt-get update && apt-get install -y wget --no-install-recommends \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-unstable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst ttf-freefont \
      --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge --auto-remove -y curl \
    && rm -rf /src/*.deb

# It's a good idea to use dumb-init to help prevent zombie chrome processes.
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 /usr/local/bin/dumb-init
RUN chmod +x /usr/local/bin/dumb-init

## / REGRESSION CSS ##

# Install node-sass and webpack globally
RUN yarn global add node-sass webpack webpack-cli grunt-cli


# Install custom helper for one command building
# COPY node_install_and_build_webpack.sh /usr/local/bin/node_install_and_build_webpack
# RUN chmod +x /usr/local/bin/node_install_and_build_webpack

# Mount projects in here and run commands here too
WORKDIR /build

