FROM thredup/ruby:2.1.6-debian

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    linux-headers-amd64 \
    python \
 && bundle config build.nokogiri --use-system-libraries

ONBUILD ARG GITHUB_TOKEN
ONBUILD ARG RAILS_ENV=production
ONBUILD ENV RAILS_ENV=${RAILS_ENV}
ONBUILD COPY Gemfile Gemfile.lock ./
ONBUILD RUN git config --global url."https://${GITHUB_TOKEN}:x-oauth-basic@github.com/".insteadOf git@github.com: \
  && bundle install --system --jobs 4 --retry 3 --without development test
