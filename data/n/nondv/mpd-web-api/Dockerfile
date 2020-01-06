FROM ruby:2.4.3-alpine

EXPOSE 6789
RUN mkdir -p /app
WORKDIR /app
COPY Gemfile Gemfile.lock /app/
RUN bundle install
COPY . /app/
CMD ["bundle", "exec", "rackup", "--host", "0.0.0.0", "-p", "6789"]
