FROM postgres:10.6-alpine
LABEL io.github.jalvcl.maintainer="jalv jlvzenzey@yahoo.com"
LABEL io.github.jalvcl.version="db_postgres_10.6_alpine"
LABEL io.github.jalvcl.repository="https://github.com/Jalvcl/03.01_Docker_Odoo_Base"
LABEL io.github.jalvcl.description="Postgres for production 10.6 build in alpine"
LABEL io.github.jalvcl.based_on="postgres Dockerfile"

VOLUME /var/lib/postgresql/data

COPY docker-entrypoint.sh /usr/local/bin/
#RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]