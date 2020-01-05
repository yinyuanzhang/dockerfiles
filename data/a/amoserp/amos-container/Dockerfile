FROM ruby:2.4.3-alpine3.7
MAINTAINER Florian Sauter <fn.sauter@gmail.com>

ENV RAILS_VERSION="5.1.5" \
    BUILD_PACKAGES="curl-dev build-base openssh" \
    DEV_PACKAGES="tzdata libxml2 libxml2-dev libxslt libxslt-dev postgresql-dev git nodejs"

RUN apk --update --upgrade add $BUILD_PACKAGES $DEV_PACKAGES
RUN npm install --global webpack
RUN apk add yarn

# GEMS
RUN \
  gem update --system && \
  gem install -N bundler && \
  gem install -N nokogiri -- --use-system-libraries && \
  gem install -N rails --version "$RAILS_VERSION" && \
  gem install -N puma && \
  echo 'gem: --no-document' >> ~/.gemrc && \
  cp ~/.gemrc /etc/gemrc && \
  chmod uog+r /etc/gemrc

# cleanup and settings
RUN \
  bundle config --global build.nokogiri  "--use-system-libraries" && \
  find / -type f -iname \*.apk-new -delete && \
  rm -rf /var/cache/apk/* && \
  rm -rf /usr/lib/lib/ruby/gems/*/cache/* && \
  rm -rf ~/.gem

# Expose port 80 to the Docker host, so we can access it
# from the outside.
EXPOSE 80
