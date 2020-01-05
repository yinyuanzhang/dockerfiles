FROM google/cloud-sdk:274.0.1-alpine

MAINTAINER Vadim Homchik <homchik@gmail.com>

ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1
ENV DATA_DIR "/data"
ENV HOST_PORT 8042

RUN apk --update --no-cache add openjdk8-jre

RUN gcloud components install beta pubsub-emulator --quiet

RUN mkdir -p ${DATA_DIR}

EXPOSE 8042

COPY run.sh /

ENTRYPOINT ["/run.sh"]
