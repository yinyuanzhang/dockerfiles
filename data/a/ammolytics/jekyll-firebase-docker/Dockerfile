FROM ammolytics/firebase-docker:latest
MAINTAINER Eric Higgins <erichiggins@gmail.com>

RUN apk upgrade --update \
  && apk add \
    ruby \
    ruby-dev \
    ruby-bundler \
    ruby-bigdecimal \
    ruby-io-console \
    ruby-irb \
    yaml \
    yaml-dev \
    ruby-json \
    ruby-rake \
  && gem install --no-document \
    bundler \
    sass \
    safe_yaml \
    jekyll \
    jekyll-paginate \
    jekyll-sass-converter \
    jekyll-sitemap \
    jekyll-feed \
    jekyll-redirect-from \
  && gem cleanup

