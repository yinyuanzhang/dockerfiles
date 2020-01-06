# Base image:
FROM ruby:2.4.4
MAINTAINER kill5038(kill5038@gmail.com)

# Install dependencies
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
RUN mkdir /run-data
# Set an environment variable where the Rails app is installed to inside of Docker image:
RUN mkdir -p /wannago
# Set working directory, where the commands will be ran:
WORKDIR /wannago
# Gems:
RUN bundle config github.https true
COPY Gemfile /wannago/Gemfile
COPY Gemfile.lock /wannago/Gemfile.lock
RUN gem install bundler -v 1.17.3
RUN bundle install --jobs 20 --retry 5 --without development test
RUN gem install foreman compass

ENV NAVER_KEY RZxc0f_jT4PDX3E6yiKT
ENV NAVER_SECRET EcFf3w7WcK
ENV RAILS_ENV production
ENV RACK_ENV production


ENV IAMPORT_CODE imp46804586
ENV IAMPORT_KEY 0018519248828949
ENV IAMPORT_SECRET Ww1fO24O4cHAmHRRBG4uEus79jbBQ3eMAg1oi5dniVYFCPwdvBIa5aheusQkw566l8vDeI1wDZbgPIuk

ENV SENTRY_DSN https://56a95399edb34cf5b0f3328c9d0203fa:3259bf4db15e4d179e883dd71df65e78@sentry.io/1367497

ENV DATABASE_URL mysql2://cgmap:madx1090!@wannago.cyjfoddc4tl6.ap-northeast-1.rds.amazonaws.com:3306/cultureground?pool=5&timeout=5000&encoding=utf8
ENV SECRET_KEY_BASE wpqkfehlfkwpqkfassaddasfat2523k5jh2jk24jl52

ENV AWS_ACCESS_KEY_ID AKIAIWZC6NAL2WXAERRA
ENV AWS_SECRET_ACCESS_KEY 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
ENV AWS_FOG_DIRECTORY wannago-prod

COPY . /wannago
RUN bundle config --global github.https true
RUN bundle exec rake assets:precompile
#RUN rake db:migrate

EXPOSE 3000
CMD ["bundle", "exec", "puma", "-C", "config/puma.rb"]
#CMD foreman start -f Procfile.production
