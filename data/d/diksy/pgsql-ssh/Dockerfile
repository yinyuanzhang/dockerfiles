FROM debian:stretch
MAINTAINER Diksy M. Firmansyah <diksy@unej.ac.id>
ENV DEBIAN_FRONTEND noninteractive

# update timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Jakarta /etc/localtime
RUN dpkg-reconfigure tzdata
# update OS
RUN sed -i s/deb.debian.org/mirror.unej.ac.id/g /etc/apt/sources.list
RUN apt-get update
RUN apt-get dist-upgrade -y
# install apps
RUN apt-get install -y supervisor sudo postgresql-9.6 openssh-server net-tools
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.6/main/postgresql.conf
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.6/main/pg_hba.conf
RUN mkdir /var/run/postgresql/9.6-main.pg_stat_tmp/
RUN chown -R postgres:postgres /var/run/postgresql/9.6-main.pg_stat_tmp/
RUN mkdir /var/run/sshd/
# add config
ADD ./pgsql-ssh.conf /etc/supervisor/conf.d/

VOLUME ["/var/lib/postgresql/9.6/main/", "/root/.ssh/", "/var/log/supervisor/"]
EXPOSE 5432 22
ENTRYPOINT ["/usr/bin/supervisord", "-n"]
