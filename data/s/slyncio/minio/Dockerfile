FROM minio/minio

ENV MINIO_ACCESS_KEY=test-access-key \
    MINIO_SECRET_KEY=test-secret-key

EXPOSE 9000

CMD ["minio", "server", "/data"]
