FROM openjdk:8-alpine

RUN mkdir -p /usr/photon
COPY photon-0.3.1.jar /usr/photon/
WORKDIR /usr/photon

CMD ["sh", "-c", "java -jar photon-0.3.1.jar -data-dir $DATA_DIR"]
