##################################### ONCE #####################################

# Base image.
FROM ruby:2.6.4-slim

# Install required packages.
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential curl default-libmysqlclient-dev git wget

# Install nodejs and yarn
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs

# Install dockerize.
ENV DOCKERIZE_VERSION v0.6.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz


# Create a working directory.
RUN mkdir /dodona/
WORKDIR /dodona/

# Clone the repository.
RUN git clone --single-branch --branch develop https://github.com/dodona-edu/dodona.git /dodona/
# Install the required gems.
RUN gem install bundler:2.0.2
RUN bundler install --without test --without production
# Install node packages.
RUN npm install -g yarn
RUN yarn install

# Set the Rails environment.
ENV RAILS_ENV="development"

# Make the webserver accessible.
EXPOSE 3000

#################################### ALWAYS ####################################

# Update the latest version of the repository.
CMD git pull origin develop \
# Patch the database host.
  && sed -i 's/localhost/database/' config/database.yml \
# Patch the database seeds: Clone over https.
  && sed -i 's+git@github.com:dodona-edu/+https://github.com/dodona-edu/+g' db/seeds.rb \
# Patch the database seeds: Use the public java judge instead of the private python judge.
  && sed -i 's/judge-pythia.git/judge-java.git/' db/seeds.rb \
# Install the required gems.
  && bundler install --without test --without production \
# Install node packages.
  && yarn install \
# Wait until the database node is active, create the database.
  && dockerize -wait tcp://database:3306 -timeout 1m bin/rails db:migrate \
# Seed the database.
  && bin/rails db:seed \
# Start the server.
  && bin/rails server -b 0.0.0.0
