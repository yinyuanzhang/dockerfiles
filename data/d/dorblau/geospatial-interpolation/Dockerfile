FROM rocker/geospatial:latest

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    gdal-bin \
    python-gdal\
    python-gribapi\
    python-pip \
    cmake\
    wget

RUN pip install six
RUN pip install cdsapi 

RUN install2.r --error \
    gdalUtils \
    geosphere \
    leaflet \
    devtools \
  && R -e "remotes::install_github('16EAGLE/getSpatialData')"

