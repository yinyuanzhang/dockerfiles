FROM sogis/qgis-server-base:3.4

# copy .qgs and .gpkg for dummy data
COPY qgis /data

RUN chown -R www-data:www-data /data

#pg_service.conf File
COPY pg/pg_service.conf /etc/postgresql-common/pg_service.conf
ENV PGSERVICEFILE="/etc/postgresql-common/pg_service.conf"

#sed command to change URL rewrite
RUN sed -i 's/\^\/qgis\//\^\/wms\//g' /etc/apache2/sites-enabled/qgis-server.conf

#tell apache/qgis-server where to find the pg_service.conf file
RUN echo 'SetEnv PGSERVICEFILE "/etc/postgresql-common/pg_service.conf"' > /etc/apache2/mods-enabled/env.conf

HEALTHCHECK --interval=30s --timeout=10s --start-period=60s CMD curl http://localhost
