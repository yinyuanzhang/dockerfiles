FROM postgres:11-alpine
MAINTAINER "Matt Critchlow <mcritchlow@ucsd.edu>"
ENV POSTGRES_USER dams
ENV POSTGRES_PASSWORD dams

ADD dams.triplestore /docker-entrypoint-initdb.d/
ADD init-dams-db.sh /docker-entrypoint-initdb.d/
