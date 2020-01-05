FROM postgres:11
ARG VCS_REF
ARG BUILD_DATE


LABEL org.label-schema.vcs-ref=$VCS_REF \
          org.label-schema.vcs-url="https://github.com/mloftis/sevend-postgis" \
          org.label-schema.build-date=$BUILD_DATE \
          org.label-schema.schema-version="1.0"


RUN apt-get update
RUN apt-get install -y --no-install-recommends postgresql-11-postgis-2.5 postgresql-11-postgis-2.5-scripts postgis postgresql-11-pgrouting postgresql-11-pgrouting-scripts

