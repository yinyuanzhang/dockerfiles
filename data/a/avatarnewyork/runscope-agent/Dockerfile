FROM frolvlad/alpine-glibc
# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=${BUILD_DATE} \
          org.label-schema.name="runscope-agent" \
          org.label-schema.description="alpine based light-weight Docker image for running the Runscope Radar on-premise agent" \
          org.label-schema.url="https://github.com/avatarnewyork/runscope-agent" \
          org.label-schema.vcs-ref=${VCS_REF} \
          org.label-schema.vcs-url="https://github.com/avatarnewyork/runscope-agent" \
          org.label-schema.vendor="" \
          org.label-schema.version=${VERSION} \
          org.label-schema.schema-version="v1.0"

RUN apk --no-cache add --update bash curl openssl tar gzip ca-certificates

RUN wget https://s3.amazonaws.com/runscope-downloads/runscope-radar/latest/linux-amd64/runscope-radar.zip && unzip -d /usr/local/bin runscope-radar.zip && \
    /bin/touch /runscope.conf


ENTRYPOINT [ "runscope-radar" ]
CMD [ "-h" ]
