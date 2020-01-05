FROM ruby:2.4.1

MAINTAINER hahaman

RUN mkdir /app \
    && chown -R nobody:nogroup /app \
	&& chmod 600 /etc/passwd \
	&& gem install cassandra-web -v 0.5.0

WORKDIR /app

ADD entrypoint.sh /app

RUN chmod 775 /app/entrypoint.sh

EXPOSE 3000

USER nobody

ENTRYPOINT ["/app/entrypoint.sh"]
