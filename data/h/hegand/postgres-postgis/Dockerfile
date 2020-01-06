FROM hegand/postgres:9.5
  
ENV POSTGIS_VERSION 2.2.2
 
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

RUN apk add --update --no-cache postgresql-dev=${PG_VERSION} \
                                perl file geos@testing geos-dev@testing  \
                                libxml2-dev gdal@testing gdal-dev@testing \
                                proj4@testing proj4-dev@testing \
                                gcc make libgcc g++ && \
    cd /tmp && \
    wget http://download.osgeo.org/postgis/source/postgis-${POSTGIS_VERSION}.tar.gz -O - | tar -xz && \
    chown root:root -R postgis-${POSTGIS_VERSION} && \
    cd /tmp/postgis-${POSTGIS_VERSION} && \
    ./configure && \
    echo "PERL = /usr/bin/perl" >> extensions/postgis/Makefile && \
    echo "PERL = /usr/bin/perl" >> extensions/postgis_topology/Makefile && \
    make -s && \ 
    make -s install  && \
    cd / && \
    rm -rf /tmp/postgis-${POSTGIS_VERSION} && \
    apk del postgresql-dev perl file geos-dev \
            libxml2-dev gdal-dev proj4-dev \
            gcc make libgcc g++
            
EXPOSE 5432

CMD ["postgres"]
