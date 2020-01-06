FROM google/cloud-sdk:alpine

RUN apk add --no-cache openjdk7-jre
RUN gcloud components install beta pubsub-emulator --quiet
RUN gcloud components update --quiet
RUN mkdir -p /tmp/emulators/pubsub

VOLUME /tmp/emulators/pubsub
EXPOSE 8085

CMD ["gcloud", "beta", "emulators", "pubsub", "start", "--data-dir", "/tmp/emulators/pubsub", "--host-port", "0.0.0.0:8085", "--verbosity", "debug"]
