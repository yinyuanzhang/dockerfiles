FROM ubuntu:16.04

MAINTAINER Marcelo França <marcelofrancaneves@hotmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y python-software-properties software-properties-common wget net-tools vim supervisor sudo 
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN wget -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
	apt-key add -
RUN apt-get update
RUN apt-get install postgresql-9.5 postgresql-client-9.5 postgresql-contrib-9.5 -y
RUN apt-get clean autoclean && apt-get autoremove -y

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY pg_hba.conf /etc/postgresql/9.5/main/pg_hba.conf
COPY postgresql.conf /etc/postgresql/9.5/main/postgresql.conf 

RUN echo "postgres ALL=(ALL) NOPASSWD:/usr/bin/supervisord" >> /etc/sudoers
RUN mkdir -p /var/log/supervisor
USER postgres

RUN /etc/init.d/postgresql start && psql --command "CREATE USER adminapp WITH SUPERUSER PASSWORD '123Mudar';" && createdb -O adminapp app1 && createdb -O adminapp app2

ENV TERM xterm

EXPOSE 5432 

CMD ["/usr/bin/sudo", "/usr/bin/supervisord"]
