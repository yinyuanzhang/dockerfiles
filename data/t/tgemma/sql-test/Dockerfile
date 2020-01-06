FROM alpine

COPY test_mysql_connection.sh /tmp/

RUN apk update && \
  apk add mysql-client

CMD sh /tmp/test_mysql_connection.sh
