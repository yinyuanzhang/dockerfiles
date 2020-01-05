FROM postgres:9.5
VOLUME /var/lib/postgresql/data
RUN chmod 777 /var/lib/postgresql/data
RUN apt-get -y update && apt-get install -y postgresql-9.5-postgis-2.2 postgresql-server-dev-9.5
USER 1002
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["postgres"]
