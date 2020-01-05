FROM ruby:2.6.2-alpine

ENV APP_HOME /gameroom-admin
ENV BUNDLER_VERSION 2.0.1

RUN apk add --no-cache --update build-base \
                                linux-headers \
                                git \
                                postgresql-dev \
                                nodejs \
                                yarn \
                                tzdata

RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD Gemfile* $APP_HOME/
RUN gem update --system
RUN gem install bundler
RUN bundle install

ADD . $APP_HOME

ADD package.json yarn.lock $APP_HOME/
RUN yarn install

COPY docker-entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]
EXPOSE 3000

CMD ["bundle", "exec", "rails", "s", "-b", "0.0.0.0"]
