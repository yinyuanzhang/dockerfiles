FROM postgres:9.6

ENV PGDATA /data
ENV POSTGRES_DB lark
ENV POSTGRES_USER lark
ENV POSTGRES_PASSWORD pg_pass
ENV POSTGRES_HOST postgres

#add init sql scripts

ADD *.sql /docker-entrypoint-initdb.d/
