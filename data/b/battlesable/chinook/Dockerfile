FROM postgres:10 AS build
ENV POSTGRES_PASSWORD=chinook

#Changing the PGDATA so that it is not created in the /var/lib/postgresql/data dir which is a volume
#because when commiting an image, data in volumes are scraped
ENV PGDATA=/var/lib/postgresql/chinook

COPY ./Chinook_PostgreSql.sql /docker-entrypoint-initdb.d/

#Remove the last line from the entrypoint script so that the database is not started.
RUN sed -i '$ d' /usr/local/bin/docker-entrypoint.sh
RUN bash /docker-entrypoint.sh postgres

FROM postgres:10
ENV PGDATA=/var/lib/postgresql/chinook
ENV POSTGRES_PASSWORD=chinook
COPY --chown=root --from=build /var/lib/postgresql/chinook /var/lib/postgresql/chinook