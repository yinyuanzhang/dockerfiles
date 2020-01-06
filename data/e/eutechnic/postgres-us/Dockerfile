# Install PostgreSQL 9.6 with en_US.UTF-8 locale
FROM postgres:9.6
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

# Expose the PostgreSQL port
EXPOSE 5432

RUN mkdir /dbdata && touch /dbdata/x
RUN chown -R postgres:postgres /dbdata
VOLUME /dbdata
