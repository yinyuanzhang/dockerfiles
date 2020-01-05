FROM flexberry/alt.p8-postgresql

COPY . /docker/

ARG TAG=1.0.0-beta02-postgresql
RUN cd /docker/host/ ; \ 
  wget https://raw.githubusercontent.com/Flexberry/FlexberryEmberTestStand.ODataBackend/$TAG/SQL/PostgreSql.create.sql  ; \
  wget https://raw.githubusercontent.com/Flexberry/FlexberryEmberTestStand.ODataBackend/$TAG/SQL/PostgreSql.insert.sql  ; \
  /bin/sh /docker/host/createdb.sh

MAINTAINER mail@flexberry.net
