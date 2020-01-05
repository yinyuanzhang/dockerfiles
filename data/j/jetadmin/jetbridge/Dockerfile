FROM python:3.7.2-alpine

RUN \
 apk add --no-cache postgresql-libs mariadb-dev jpeg-dev zlib-dev && \
 apk add --no-cache --virtual .build-deps gcc g++ musl-dev postgresql-dev unixodbc-dev

RUN apk add --no-cache --virtual .build-deps-testing \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
    gdal-dev \
    geos-dev \
    proj-dev

#RUN addgroup -S jet && adduser -S -G jet jet
RUN pip install psycopg2 mysqlclient pyodbc
RUN pip install GeoAlchemy2==0.6.2 Shapely==1.6.4

COPY packages /packages
RUN pip install -e /packages/jet_bridge_base
RUN pip install -e /packages/jet_bridge

RUN mkdir /jet
VOLUME /jet
WORKDIR /jet

#USER jet

COPY docker/entrypoint.sh /
COPY docker/network-entrypoint.sh /
RUN chmod +x /entrypoint.sh
RUN chmod +x /network-entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
