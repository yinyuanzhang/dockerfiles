FROM postgres:9.5-alpine
ENV POSTGRES_USER postgres
ENV POSTGRES_DB fudge
COPY init.sql.gz /docker-entrypoint-initdb.d/