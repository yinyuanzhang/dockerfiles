FROM ruby:2.3

RUN gem install cassandra-web

ENV CASSANDRA_HOST="127.0.0.1" \
    CASSANDRA_PORT="9042" \
    CASSANDRA_USERNAME="cassandra" \
    CASSANDRA_PASSWORD="cassandra" \
    WEB_UI_PORT="80"

ADD entrypoint.sh /

RUN chmod a+x /entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
