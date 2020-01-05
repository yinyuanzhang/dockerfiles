FROM ruby:2.4.6-alpine
LABEL author="Nossas<tech@nossas.org>"

ENV PACKAGES postgresql-dev libxml2-dev libxslt-dev openssl libpq libffi-dev bash curl libstdc++ tzdata bash ca-certificates build-base ruby-dev libc-dev linux-headers postgresql-client postgresql
# ENV RUBY_PACKAGES ruby ruby-io-console ruby-bundler ruby-irb ruby-bigdecimal ruby-json
ENV RAILS_ENV=production RACK_ENV=production DISABLE_SSL=true

# Update and install all of the required packages.
# At the end, remove the apk cache
# RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.7/main' >> /etc/apk/repositories
RUN apk add --no-cache --update $PACKAGES

RUN mkdir /usr/app
WORKDIR /usr/app

COPY Gemfile /usr/app/
COPY Gemfile.lock /usr/app/

RUN bundle install
COPY . /usr/app

CMD [ "bundle", "exec", "puma", "-C", "config/puma.rb" ]

EXPOSE 3000

RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && echo "America/Sao_Paulo" >  /etc/timezone

# ==================================================================================================
# 7: Copy the rest of the application code, install nodejs as a build dependency, then compile the
# app assets, and finally change the owner of the code to 'nobody':
RUN set -ex \
  && mkdir -p /usr/app/tmp/cache \
  && mkdir -p /usr/app/tmp/pids \
  && mkdir -p /usr/app/tmp/sockets
#  && chown -R nobody /usr/app

# ==================================================================================================
# 8: Set the container user to 'nobody':
#USER nobody
