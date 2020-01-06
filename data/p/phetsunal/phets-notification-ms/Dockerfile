FROM ruby:2.5
RUN apt-get update -qq && apt-get install -y nodejs postgresql-client
RUN mkdir /phets-notification-ms
WORKDIR /phets-notification-ms
COPY Gemfile /phets-notification-ms/Gemfile
COPY Gemfile.lock /phets-notification-ms/Gemfile.lock
RUN bundle install
COPY . /phets-notification-ms

# Add a script to be executed every time the container starts.
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 4004

# Start the main process.
CMD ["rails", "server", "-b", "0.0.0.0", "-p", "4004"]