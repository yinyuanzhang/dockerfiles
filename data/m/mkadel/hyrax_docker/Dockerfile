# Use an official Ruby as parent image
FROM ruby:2.6.2

# Install apt based dependencies required to run Rails
RUN apt-get update && apt-get install -y \
  build-essential \
  nodejs \
  apt-utils

# Set the working directory to /app
RUN mkdir -p /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY Gemfile Gemfile.lock ./

# update bundle installer
RUN gem install bundler && bundle install --jobs 20 --retry 5

# Copy the main application.
COPY . ./

# Expose port 3000 to the Docker host, so we can access it from the outside.
EXPOSE 3000

# The main command to run when the container starts. Also
# tell the Rails dev server to bind to all interfaces by
# default.
CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]
