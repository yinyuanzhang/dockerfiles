# Latest ruby 2.3 image as base
FROM ruby:2.3

EXPOSE 3000

# Supervisor will execute both services properly
RUN apt-get update \
 && apt-get install -y less nano \
    supervisor \
    redis-server \
 && apt-get clean

WORKDIR /app

RUN bundle config --global frozen 1
# Copy dependencies and install them
COPY Gemfile Gemfile.lock Guardfile Rakefile config.ru ./
RUN bundle install
# Copy rest of the application
COPY .env-docker .env
COPY ./app app
COPY ./bin bin
COPY ./config config
COPY ./db db
COPY ./lib lib
COPY ./public public

# Topic: Seeding
# rake db:reset cannot be run in the construciton phase of the conainer. It needs mongoDB running.
# rake db:reset for initial db setup
# rake db:seed:<seed_file> for seeding of files
# rake db:seed:formula for a formula example

# Configure supervisord
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Start server and delete old pid files before, rails doesn't clean up
# CMD /bin/sh -c 'rm -f /app/tmp/pids/server.pid && rails s'

# Start up supervisor to run the server and necessary side processes like redis and sidekiq
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
