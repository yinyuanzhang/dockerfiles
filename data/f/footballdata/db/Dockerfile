FROM python:3.6.3-alpine as build_prep

WORKDIR /app
ADD . /app

RUN python ./deploy.py -m pack

FROM postgres:alpine
COPY --from=build_prep /app/tmp_build /app/tmp_build
COPY --from=build_prep /app/admin /app/admin
COPY --from=build_prep /app/init-db.sh /docker-entrypoint-initdb.d/init-db.sh

