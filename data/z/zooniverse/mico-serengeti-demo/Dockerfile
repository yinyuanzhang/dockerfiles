FROM zooniverse/ruby:2.2.1

WORKDIR /rails_app

ENV DEBIAN_FRONTEND noninteractive
ENV RAILS_SERVE_STATIC_FILES true

RUN apt-get update && apt-get -y upgrade && \
    apt-get install --no-install-recommends -y git curl supervisor  && \
    apt-get clean

ADD ./Gemfile /rails_app/
ADD ./Gemfile.lock /rails_app/

RUN bundle install --without development test

ADD supervisord.conf /etc/supervisor/conf.d/mico-serengeti-demo.conf
ADD ./ /rails_app

EXPOSE 80

ENTRYPOINT /rails_app/scripts/docker/start.sh
