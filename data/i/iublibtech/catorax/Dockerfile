# system dependency image
FROM ruby:2.5 AS catorax-sys-deps

# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1

RUN apt-get update -qq && \
    apt-get install -y build-essential default-jre-headless libpq-dev nodejs libreoffice-writer libreoffice-impress imagemagick unzip ghostscript && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir -p /opt/fits && \
    curl -fSL -o /opt/fits/fits-1.3.0.zip http://projects.iq.harvard.edu/files/fits/files/fits-1.3.0.zip && \
    cd /opt/fits && unzip fits-1.3.0.zip && chmod +X fits.sh
ENV PATH /opt/fits:$PATH

# ruby dependencies image
FROM catorax-sys-deps AS catorax-deps

RUN mkdir /app
WORKDIR /app

COPY Gemfile Gemfile.lock ./
RUN gem update bundler
RUN bundle install -j 2 --retry=3 --deployment --without development

COPY . .

ENV RAILS_LOG_TO_STDOUT true
ENV RAILS_ENV production

ENTRYPOINT ["bundle", "exec"]

# sidekiq image
FROM catorax-deps as catorax-sidekiq
ARG SOURCE_COMMIT
ENV SOURCE_COMMIT $SOURCE_COMMIT
CMD sidekiq

# webserver image
FROM catorax-deps as catorax-web
RUN bundle exec rake assets:precompile
EXPOSE 3000
ARG SOURCE_COMMIT
ENV SOURCE_COMMIT $SOURCE_COMMIT
CMD puma -b tcp://0.0.0.0:3000
