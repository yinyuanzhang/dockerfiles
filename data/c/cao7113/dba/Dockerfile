FROM ruby:2.4.4-alpine3.6
RUN apk update && apk add build-base postgresql postgresql-dev
# RUN apk add --no-cache postgresql-client

WORKDIR /app
COPY Gemfile ./
#ENV GEM_SOURCE=http://docker.for.mac.host.internal:8808
#RUN bundle install --without development test --verbose
RUN bundle install --verbose

COPY . /app
ENV PATH=/app/bin:$PATH
CMD sh
