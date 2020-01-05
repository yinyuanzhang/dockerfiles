
# The installer
FROM postgres:10-alpine as installer

ENV PGAMQPVERSION v0.4.1

RUN pg_config --libdir

RUN apk -U add \
    alpine-sdk \
    perl \
    build-base \
 && git config --global user.email "user@docker" \
 && git config --global user.name "user" \
 && git config --global advice.detachedHead false \
 && git clone https://github.com/omniti-labs/pg_amqp.git pg_amqp \
 && cd pg_amqp \
 && git checkout ${PGAMQPVERSION}

COPY ./patches/* /patches/
RUN cd pg_amqp \
 && git am /patches/pg_amqp_*

RUN cd pg_amqp \
 && make \
 && make install

RUN ls -la /usr/local/share/postgresql/extension/


# The image
FROM postgres:10-alpine

COPY --from=installer /usr/local/share/postgresql/extension/amqp* /usr/local/share/postgresql/extension/
COPY --from=installer /usr/local/lib/postgresql/pg_amqp* /usr/local/lib/postgresql/

COPY ./docker-entrypoint-initdb.d/* /docker-entrypoint-initdb.d/
COPY ./scripts/* /scripts/
RUN chmod +x /scripts/*

LABEL maintainer="Tuomas Lehtonen" \
      description="PIM postgres image" \
      version="10-alpine"

COPY pim-docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/pim-docker-entrypoint.sh / # backwards compat
RUN chmod +x pim-docker-entrypoint.sh
ENTRYPOINT ["pim-docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]
