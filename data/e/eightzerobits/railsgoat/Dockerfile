FROM ruby:2.6.2
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs

COPY . /app
WORKDIR /app
RUN bundle install \
	&& rake db:setup 

CMD ["rails", "server", "-b", "0.0.0.0"]
