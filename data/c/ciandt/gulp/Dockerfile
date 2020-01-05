FROM node:8.12.0-slim

### baseline configuration for all debian/ubuntu dockers
# use bash, no dash
RUN ln --symbolic --force /bin/bash /bin/sh

# update debian/ubuntu and install basic tools
RUN apt-get update && apt-get upgrade --assume-yes && apt-get install --no-install-recommends --assume-yes \
    vim \
    screen \
    git \
    ruby-full
## end of baseline

### specific configuration
# gulp variables
ENV _GULP_VERSION 2.0.1

# install libraries
RUN apt-get install --no-install-recommends --assume-yes \
    libpng12-0

# install gulp
RUN npm install --global gulp-cli@$_GULP_VERSION

# install scss-lint
# RUN gem install scss_lint

# copy entrypoint scripts
COPY files/docker-entrypoint.sh /entrypoint.sh

# define default workdir
RUN mkdir /tmp/run
WORKDIR /tmp/run

# define entrypoint and default cmd
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gulp"]
