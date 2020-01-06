# This file is a template, and might need editing before it works on your project.
FROM ruby:2.3-slim-jessie

# Edit with nodejs, mysql-client, postgresql-client, sqlite3, etc. for your needs.
# Or delete entirely if not needed.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        make \
        python2.7 \
        openssh-client \
        rsync \
        git \
    && rm -rf /var/lib/apt/lists/*

# Make python2.7 the default system version
RUN ln -sf /usr/bin/python2.7 /usr/bin/python

# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1

WORKDIR /usr/src/app

COPY Gemfile Gemfile.lock /usr/src/app/
RUN bundle install -j $(nproc)

#COPY . /usr/src/app

# For Sinatra
#EXPOSE 4567
#CMD ["ruby", "./config.rb"]

# For Rails
#EXPOSE 3000
#CMD ["rails", "server", "-b", "0.0.0.0"]
