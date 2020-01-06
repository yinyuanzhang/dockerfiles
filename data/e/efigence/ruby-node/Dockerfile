FROM starefossen/ruby-node:2-8

RUN apt-get update
RUN apt-get install -y -qq libpq-dev cmake
RUN gem install bundler --no-ri --no-rdoc
RUN bundle config without production
RUN bundle config path cache/bundler

COPY vendor vendor

COPY Gemfile Gemfile.lock ./
RUN bundle install --jobs $(nproc) --without=production

COPY package.json yarn.lock ./
RUN \
  yarn install --no-emoji --frozen-lockfile && \
  mv ./node_modules /usr/local/node_modules
