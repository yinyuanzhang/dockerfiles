FROM ruby:2.5-alpine
ARG slate_version=v2.3.1

RUN apk add --no-cache coreutils git make g++ nodejs

RUN git clone https://github.com/lord/slate && \
    cd /slate && git checkout $slate_version && \
    rm -rf .git && \
    mv /slate/source /slate/source_orig

RUN cd /slate && \
    echo "gem 'middleman-livereload', '~> 3.4.3'" >> Gemfile && \
    bundle install --no-cache

RUN echo "activate :livereload, js_host: 'localhost'" >> /slate/config.rb

VOLUME /slate/source
VOLUME /slate/build

EXPOSE 4567
EXPOSE 35729

CMD cd /slate && cp -nr source_orig/* source && exec bundle exec middleman server --watcher-force-polling
