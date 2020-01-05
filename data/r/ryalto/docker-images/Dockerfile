FROM postgres:9.5
MAINTAINER paul@trippett.org

COPY files/postgres-docker-entrypoint.sh /docker-entrypoint.sh

EXPOSE 5432

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["postgres"]
