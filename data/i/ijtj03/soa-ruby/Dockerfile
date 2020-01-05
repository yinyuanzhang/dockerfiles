FROM ruby:2.5

# Set the Current Working Directory inside the container
WORKDIR /SOA_RUBYGRAPHQL

# Copy everything from the current directory to the PWD(Present Working Directory) inside the container
COPY . .

RUN gem install bundler

RUN gem install rails

RUN bundle install

# This container exposes port 8080 to the outside world
EXPOSE 3000
