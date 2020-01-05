FROM google/cloud-sdk:alpine
RUN apk --update add openjdk7-jre
RUN gcloud components install beta cloud-datastore-emulator
CMD gcloud beta emulators datastore start --consistency=1.0 --no-store-on-disk --host-port 0.0.0.0:8081 --project fake-project-id
EXPOSE 8081
