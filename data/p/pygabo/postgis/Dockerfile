FROM postgres:11.5

RUN apt-get update \
    && apt-get install wget -y \
    && apt-get install postgresql-11-postgis-2.5 -y \
    && apt-get install postgresql-11-postgis-scripts -y \
    && apt-get install postgis -y
