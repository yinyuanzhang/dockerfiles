FROM ruby:2.6-alpine

RUN apk add build-base postgresql-client postgresql-dev yarn git
RUN apk update && apk add -u yarn

WORKDIR /home/meltingpot/

# Install Dependencies for Node and Ruby
COPY Gemfile Gemfile.lock ./
RUN bundle install --jobs=4
COPY package.json yarn.lock ./
RUN yarn install

# Expose
EXPOSE 3000

# Copy All Code
COPY . . 

# Generate Static 
RUN NODE_OPTS="--max-old-space-size=1024" rake assets:precompile

VOLUME ["/home/meltingpot"]

# Run the server
CMD ["rails", "s"]
