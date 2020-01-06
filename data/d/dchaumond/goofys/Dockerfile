FROM ubuntu:16.04

# just some environment variables
ENV AWS_ACCESS_KEY ''
ENV AWS_SECRET_KEY ''
ENV S3_BUCKET ''
ENV S3_REGION ''
ENV MOUNT_PATH '/data'

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
            # DCH: REQUIRED FOR goofys
            openssl ca-certificates \
            # s3fs dependencies \
            automake autotools-dev fuse g++ git libcurl4-gnutls-dev libfuse-dev \
            libssl-dev libxml2-dev make pkg-config \
            # finally, clean up to make image smaller \
            && apt-get clean

RUN mkdir /app
RUN mkdir $MOUNT_PATH
COPY ./goofys /app
RUN chmod 775 /app/goofys
WORKDIR /app
CMD exec ./goofys --region $S3_REGION $S3_BUCKET $MOUNT_PATH
