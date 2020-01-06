# 1: Use ruby 2.3.1 as base:
FROM securable/backend-base-image:1.0.1

# 2: We'll set the application path as the working directory
WORKDIR /usr/src/app

# 3: We'll add the app's binaries path to $PATH:
ENV HOME=/usr/src/app PATH=/usr/src/app/bin:$PATH

# 5: Install the current project gems - they can be safely changed later
# during development via `bundle install` or `bundle update`:
COPY . /usr/src/app/
RUN set -ex && bundle install

# Because cross-linking still hasn't been resolved after 3+ years
RUN set -ex && cd ./client && mv ./node_modules ./node_modules.tmp && mv ./node_modules.tmp ./node_modules && npm install

# RUN set -ex && cd ./client && npm run production
RUN DB_ADAPTER=nulldb RAILS_ENV=production SECRET_KEY_BASE=abc rake assets:clobber assets:precompile --trace
