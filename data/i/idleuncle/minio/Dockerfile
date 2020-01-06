FROM alpine:3.9

ADD https://dl.min.io/server/minio/release/linux-amd64/minio /usr/bin/
COPY healthcheck.sh /usr/bin/
COPY docker-entrypoint.sh /usr/bin/

ENV MINIO_UPDATE off
ENV MINIO_ACCESS_KEY_FILE=access_key \
    MINIO_SECRET_KEY_FILE=secret_key

EXPOSE 9000

ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]

VOLUME ["/data"]

HEALTHCHECK --interval=30s --timeout=5s CMD /usr/bin/healthcheck.sh

CMD ["/usr/bin/minio"]
