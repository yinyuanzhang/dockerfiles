ARG POSTGRES_VERSION=11
FROM postgres:$POSTGRES_VERSION

RUN apt-get update && apt-get install -y tzdata

RUN rm /etc/localtime
RUN ln -s /usr/share/zoneinfo/Etc/GMT /etc/localtime
RUN date

RUN apt-get update \
	&& apt-get install -y wget \
	&& apt-get install -y zip \
	&& apt-get install -y postgresql-server-dev-11 \
	&& apt-get install -y libpq-dev \
	&& apt-get install -y build-essential

ADD postgresql.conf /etc/postgresql.conf
RUN chmod 777 /etc/postgresql.conf

COPY 00-create-extensions.sql /docker-entrypoint-initdb.d/
RUN chmod 755 /docker-entrypoint-initdb.d/00-create-extensions.sql

RUN mkdir /var/pg_backups/
RUN chmod 777 -R /var/pg_backups
ADD pg_util /var/pg_util


USER postgres

CMD ["postgres","-c","config_file=/etc/postgresql.conf"]