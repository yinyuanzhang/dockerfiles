FROM library/ruby:2.3.1
MAINTAINER Roy Tsang <me@roytsang.com>

ENV COMPOSE=1
ENV RAILS_ENV=production
ENV RACK_ENV="production"
ENV CATALOG_CRON="5"
EXPOSE 3000

WORKDIR /portus
COPY portus/Gemfile* ./
RUN bundle install --retry=3 && bundle binstubs phantomjs
RUN apt-get update && \
    apt-get install -y --no-install-recommends nodejs

ADD portus .

# Copy scipt files
COPY check_db.rb /
COPY init /
RUN chmod +x /init

# Run this command to start it up
ENTRYPOINT ["/bin/bash","/init"]
