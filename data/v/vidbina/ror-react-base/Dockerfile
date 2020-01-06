FROM vidbina/ror:latest
ADD Gemfile Gemfile
ADD Gemfile.lock Gemfile.lock
RUN bundle install && \
  npm install -g yarn
