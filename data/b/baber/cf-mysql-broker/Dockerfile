FROM ruby:2.3.1
COPY . /cf-mysql-broker
WORKDIR /cf-mysql-broker
RUN bundle install
EXPOSE 8080
CMD ["./entrypoint.sh"]
