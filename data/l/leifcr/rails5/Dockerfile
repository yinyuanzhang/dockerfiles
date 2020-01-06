FROM ruby:2.6
MAINTAINER leifcr@gmail.com

# Add https transport to apt
RUN apt-get update -qq && apt-get install -y apt-transport-https

# Install updated nodejs, yarn and build packages
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
  && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
  && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
  && apt-get update -qq && apt-get install -y \
  build-essential \
  libpq-dev \
  default-libmysqlclient-dev \
  libxml2-dev \
  libxslt1-dev \
  default-mysql-client \
  wget \
  nodejs \
  yarn \
  && apt-get install -y google-chrome-stable --no-install-recommends

# For staging and production env, duck-cli must be installed to be able to download refile assets
ENV APP_HOME /app

# If encoding errors occur, adjust locale.
ENV LANG C.UTF-8

# Create application folder and ssh-agent folder
# Setup rails user group and rails user
# Set rails:rails as user on app and ssh-agent folder
RUN mkdir $APP_HOME && \
    mkdir /ssh-agent && \
    groupadd -g 1000 rails && \
    useradd -s /bin/bash -m -d /home/rails -g rails rails && \
    chown rails:rails /app && \
    chown rails:rails /ssh-agent

# Copy docker entry point
COPY docker-entrypoint.sh /usr/local/bin/

# Make entrypoint executable when building on Windows
# And backwards compatible entrypoint
RUN chmod +x /usr/local/bin/docker-entrypoint.sh && ln -s /usr/local/bin/docker-entrypoint.sh /docker-entrypoint.sh

# Continue as rails user
USER rails

# Set workdir to /app, so COPY, ADD, RUN and ENTRYPOINT is run within folder
WORKDIR $APP_HOME

# Add Gemfile
COPY Gemfile Gemfile.lock ./
# Install gems
RUN gem install bundler --version 1.17.3 && bundle install --jobs 20 --retry 5

# Set entry point to bundle exec, as all cmd's with rails should be prepended
ENTRYPOINT ["docker-entrypoint.sh"]
