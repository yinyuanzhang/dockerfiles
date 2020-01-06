FROM ruby:2.1
MAINTAINER Aesop Agency <contact@mikefarrow.co.uk>

# Install node + npm
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - && \
    apt-get install -y \
    nodejs

ENV BUNDLE_JOBS=2 \
    BUNDLE_PATH=/bundle

VOLUME /bundle

