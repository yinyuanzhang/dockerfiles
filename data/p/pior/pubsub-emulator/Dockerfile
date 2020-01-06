FROM google/cloud-sdk:alpine

RUN apk --no-cache  --update add openjdk8-jre \
 && gcloud components install --quiet beta pubsub-emulator

EXPOSE 8085

ENTRYPOINT ["gcloud", "beta", "emulators", "pubsub", "start", "--user-output-enabled", "--host-port=0.0.0.0:8085"]
