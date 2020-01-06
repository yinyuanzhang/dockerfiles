FROM ruby:2.6.1
# Add NodeJS to sources list
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -

# Add Yarn to the sources list
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo 'deb http://dl.yarnpkg.com/debian/ stable main' > /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -qq -y curl build-essential nodejs libpq-dev ruby-dev yarn --fix-missing --no-install-recommends
WORKDIR /brand-secure
COPY . /brand-secure
COPY Gemfile /brand-secure
COPY Gemfile.lock /brand-secure
RUN gem install bundler
RUN ln -sf /usr/bin/nodejs /usr/local/bin/node
RUN bundle install
RUN yarn install
ENV PORT 3000

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod 777 /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]
