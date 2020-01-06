FROM ruby:2.5-alpine
WORKDIR /build
COPY . /build
RUN gem build logstash-output-clickhouse.gemspec -V

FROM scratch
COPY --from=0 /build/*.gem /