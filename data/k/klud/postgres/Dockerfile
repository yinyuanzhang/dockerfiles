FROM multiarch/alpine:armhf-v3.6
LABEL maintainer "Klud <pierre.ugazm@gmail.com>"
ENV LANG en_US.utf8
ENV PGDATA /var/lib/postgresql/data
RUN apk add --no-cache \
    postgresql \
    bash && \
    mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql &&\
    mkdir /docker-entrypoint-initdb.d
VOLUME /var/lib/postgresql/data
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 5432
CMD ["postgres"]