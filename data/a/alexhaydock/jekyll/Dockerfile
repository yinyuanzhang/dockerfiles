FROM ubuntu:18.04
LABEL maintainer "Alex Haydock <alex@alexhaydock.co.uk>"

# Set Locales
# (Without this we get an error about US-ASCII when
# trying to serve the site with Jekyll)
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# Install Ruby, Bundler, and anything else that the
# bundler install process below has told us we need.
RUN apt-get update && \
    apt-get install -y bundler git ruby zlib1g-dev

# Install necessary Gems
COPY Gemfile /tmp/Gemfile
WORKDIR /tmp
RUN bundle install

# Default dir for building Jekyll sites with this container
WORKDIR /opt/www
