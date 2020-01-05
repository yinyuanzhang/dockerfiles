FROM ruby:2.5.1-alpine
RUN apk --update upgrade && apk add --no-cache build-base sqlite-dev tzdata
RUN mkdir /app
WORKDIR /app
COPY ./Gemfile ./Gemfile.lock ./
RUN gem install bundler && bundle install
COPY . .
EXPOSE 3000
CMD ["bundle", "exec", "rails", "server"]