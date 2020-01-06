FROM hegand/alpine:3.5

ENV PG_MAJOR=9.6 \
    PG_VERSION=9.6.2-r0
    
ENV LANG en_US.utf8

RUN apk add --update --no-cache postgresql=${PG_VERSION} \
                                postgresql-contrib=${PG_VERSION} \
                                bash
            
RUN mkdir /docker-entrypoint-initdb.d && \
    mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql

ENV PGDATA /var/lib/postgresql/data
    
VOLUME /var/lib/postgresql/data

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5432

CMD ["postgres"]
