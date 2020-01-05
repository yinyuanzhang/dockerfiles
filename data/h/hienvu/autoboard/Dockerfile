FROM ruby:2.5.3

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs

# install cron
RUN apt-get install -y cron

# set timezone
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# set locale japanese for ubuntu
RUN apt-get update \
  && apt-get install -y locales  \
  && locale-gen ja-JP.UTF-8 \
  && localedef -f UTF-8 -i ja_JP ja_JP
ENV LANG=ja_JP.UTF-8

# install phantomjs
ARG PHANTOM_JS_VERSION
ENV PHANTOM_JS_VERSION ${PHANTOM_JS_VERSION:-2.1.1-linux-x86_64}
RUN set -x  \
  && apt-get update \
  && apt-get install -y --no-install-recommends \&& mkdir /tmp/phantomjs \
  && curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOM_JS_VERSION}.tar.bz2 \
    | tar -xj --strip-components=1 -C /tmp/phantomjs \
  && mv /tmp/phantomjs/bin/phantomjs /usr/local/bin \
  && curl -Lo /tmp/dumb-init.deb https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-init_1.1.3_amd64.deb \
  && dpkg -i /tmp/dumb-init.deb \
  && apt-get purge --auto-remove -y \
    curl \
  && apt-get clean \
  && rm -rf /tmp/* /var/lib/apt/lists/* \
  && useradd --system --uid 52379 -m --shell /usr/sbin/nologin phantomjs \
  && su phantomjs -s /bin/sh -c "phantomjs --version"

# install japanese font for phantomjs
RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y fonts-ipaexfont-gothic \
  && apt-get autoremove -y \
  && apt-get clean all

RUN mkdir /AutoBoard
WORKDIR /AutoBoard
RUN gem install bundler --version=1.17 #docker not work with bundle 2.0
ADD Gemfile /AutoBoard/Gemfile
ADD Gemfile.lock /AutoBoard/Gemfile.lock
RUN bundle install
ADD . /AutoBoard

RUN bundle exec whenever --update-crontab
#CMD ["cron", "-f"]
CMD cron && bundle exec puma
