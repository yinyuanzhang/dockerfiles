# This file is taken from: https://docs.docker.com/compose/rails/
# 2019-02-21

FROM ruby:2.5
RUN apt-get update -qq && apt-get install -y nodejs postgresql-client

RUN curl -sL https://deb.nodesource.com/setup_11.x | bash
RUN apt-get install -qq -y nodejs
RUN npm install -g yarn

RUN mkdir /app
WORKDIR /app
COPY Gemfile /app/Gemfile
COPY Gemfile.lock /app/Gemfile.lock
RUN gem install bundler -v '> 2'
RUN bundle install
COPY . /app

# Add a script to be executed every time the container starts.
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000

# Start the main process.
CMD ["rails", "server", "-b", "0.0.0.0"]