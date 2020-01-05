FROM ruby:2.5.1

RUN apt-get update; \
    apt-get upgrade -y; \
    apt-get install -y build-essential libssl-dev libreadline-dev libyaml-dev \
      default-libmysqlclient-dev gnupg2

RUN curl -o /usr/bin/framgia-ci https://raw.githubusercontent.com/framgia/ci-report-tool/master/dist/framgia-ci && chmod +x /usr/bin/framgia-ci

EXPOSE 3000

CMD ["/bin/bash"]

ENV CACHE_PATH /cache

WORKDIR $CACHE_PATH

ADD Gemfile $CACHE_PATH
ADD Gemfile.lock $CACHE_PATH

RUN bundle install --without development test \
    --jobs `expr $(cat /proc/cpuinfo | grep -c "cpu cores") - 1` \
    --retry 3

ENV LANG='en_US.UTF-8'
ENV RAILS_LOG_TO_STDOUT='enabled'
ENV RAILS_SERVE_STATIC_FILES='enabled'

COPY . $CACHE_PATH
COPY config/database.yml.docker $CACHE_PATH/config/database.yml
