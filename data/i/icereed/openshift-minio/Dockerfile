FROM centos

RUN useradd -d /opt/minio -g root minio

WORKDIR /opt/minio

ADD entrypoint.sh .

RUN curl -o minio https://dl.minio.io/server/minio/release/linux-amd64/minio && \
    chmod +x minio && \
    mkdir config && \
    mkdir data  && \
    chown minio:root -R . && chmod 777 -R .

USER minio

ENV MINIO_ACCESS_KEY="demoaccesskey"
ENV MINIO_SECRET_KEY="mysecret"
ENV MINIO_BIN=/opt/minio/minio
ENV MINIO_DATA_DIR=/opt/minio/data
ENV MINIO_CONFIG_DIR=/opt/minio/config


VOLUME $MINIO_CONFIG_DIR
VOLUME $MINIO_DATA_DIR

EXPOSE 9000

ENTRYPOINT [ "./entrypoint.sh" ]
