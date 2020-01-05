FROM google/cloud-sdk:alpine

LABEL maintainer ="travix" 
LABEL version="1.0" 
LABEL description="Google Cloud PubSub Emulator"

RUN apk --update add openjdk7-jre
RUN gcloud components install --quiet beta pubsub-emulator

EXPOSE 8085

ENTRYPOINT ["gcloud", "beta", "emulators", "pubsub"]
CMD ["start", "--host-port", "0.0.0.0:8085"]