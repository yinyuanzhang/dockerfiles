FROM ruby:2.3.8

# Install Node and other build dependencies
RUN apt-get update -y
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y build-essential libpq-dev nodejs npm postgresql imagemagick
RUN npm install -g yarn
ENV PATH=/root/.yarn/bin:$PATH

# Set an environment variable where the Rails app is installed to inside of Docker image
ENV RAILS_ROOT /app
RUN mkdir -p $RAILS_ROOT

# Set working directory
WORKDIR $RAILS_ROOT

# Adding gems
COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock

# Control if changes to the Gemfile are allowed in this build
ARG BUNDLE_FREEZE=false

# Install base dependencies
RUN bundle config --local frozen $BUNDLE_FREEZE
RUN bundle install

# Install additional dependencies
ARG INSTALL_GROUPS="test development staging"
RUN bundle install --with $INSTALL_GROUPS

# Adding project files
COPY . $RAILS_ROOT

# Control if assets are pre-compiled
# TODO: https://blog.bigbinary.com/2018/07/25/speeding-up-docker-image-build-process-of-a-rails-application.html
ARG RAILS_ENV="development"
ARG PRECOMPILE_ASSETS=false
RUN if [ $PRECOMPILE_ASSETS = true ]; then DATABASE_ADAPTER=nulldb bundle exec rake assets:precompile; fi

EXPOSE 3000

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["bundle", "exec", "rails", "server"]
