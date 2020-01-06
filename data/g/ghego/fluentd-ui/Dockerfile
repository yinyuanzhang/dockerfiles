FROM alpine:3.4

EXPOSE 24224
EXPOSE 9292

VOLUME ["/root"]

RUN apk add --update mysql
RUN apk add --update ruby ruby-dev
RUN apk add --update build-base
RUN apk add --update libssl1.0
RUN apk add --update libxml2-dev
RUN apk add --update libxslt-dev

RUN gem install --no-document rake
RUN gem install --no-document bigdecimal
RUN gem install --no-document cool.io
RUN gem install --no-document did_you_mean
RUN gem install --no-document http_parser.rb
RUN gem install --no-document io-console
RUN gem install --no-document json
RUN gem install --no-document minitest
RUN gem install --no-document msgpack
RUN gem install --no-document net-telnet
RUN gem install --no-document power_assert
RUN gem install --no-document psych
RUN gem install --no-document rdoc
RUN gem install --no-document sigdump
RUN gem install --no-document syslog_protocol
RUN gem install --no-document test-unit
RUN gem install --no-document thread_safe
RUN gem install --no-document tzinfo
RUN gem install --no-document tzinfo-data
RUN gem install --no-document uuidtools
RUN gem install --no-document yajl-ruby
RUN gem install --no-document --version 0.4.3 fluentd-ui

CMD ["fluentd-ui", "start"]
