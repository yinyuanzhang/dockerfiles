FROM nenadalm/fedora

RUN yum upgrade -y
RUN yum install -y \
    postgresql-server
RUN yum clean all

RUN rm -rf /var/lib/pgsql/data/*

USER postgres
RUN initdb --pgdata="/var/lib/pgsql/data"

COPY configuration /

USER root
RUN chown -R postgres:postgres /var/lib/pgsql/data
RUN chmod 700 /var/lib/pgsql/data

USER postgres
EXPOSE 5432
CMD postgres -D /var/lib/pgsql/data

