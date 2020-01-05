FROM centos:centos7

RUN yum install -y epel-release* && yum update -y 

RUN yum install -y which gcc gcc-c++ make wget zlib-devel openssl-devel

ENV GDAL_VERSION=2.2.1

# python
#
RUN yum install -y python-devel python-pip

RUN pip install --upgrade virtualenv

# gdal dependencies
#
RUN yum install -y hdf-devel hdf5-devel libtiff-devel libgeotiff-devel geos-devel proj-devel libpng-devel netcdf-devel

# gdal 
#
RUN wget http://download.osgeo.org/gdal/$GDAL_VERSION/gdal-${GDAL_VERSION}.tar.gz -O /tmp/gdal-${GDAL_VERSION}.tar.gz && \
    tar -x -f /tmp/gdal-${GDAL_VERSION}.tar.gz -C /tmp

RUN cd /tmp/gdal-${GDAL_VERSION} && \
    ./configure \
        --prefix=/usr/ \
        --with-hide-internal-symbols \
        --with-geos \
        --with-geotiff --with-rename-internal-geotiff-symbols=yes\
        --with-libtiff --with-rename-internal-libtiff-symbols=yes\
        --with-png \
        --with-jpeg \
        --with-openjpeg \
        --with-netcdf \
        --without-expat --without-odbc --without-sqlite3 --without-libtool --without-pg \
        --without-libkml --without-curl --without-pcre --without-xerces \
        --enable-shared \
        CFLAGS= CXXFLAGS= && \
    make -j "$(nproc)" && make install && \
    rm -rf /tmp/gdal-${GDAL_VERSION}.tar.gz && rm -rf /tmp/gdal-${GDAL_VERSION}

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/


