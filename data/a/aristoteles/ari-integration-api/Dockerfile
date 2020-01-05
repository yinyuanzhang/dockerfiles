FROM maven:3-jdk-8-slim

ENV AWS_REGION ''
ENV AWS_KEY ''
ENV AWS_SECRET_KEY ''
ENV CONFIG_SERVER_PORT 7000

RUN mkdir /workspace
COPY ./ /workspace

RUN mvn install:install-file -Dfile=/workspace/TranskribusClient-0.0.6.jar -DgroupId=eu.transkribus -DartifactId=TranskribusClient -Dversion=0.0.6 -Dpackaging=jar
RUN mvn install:install-file -Dfile=/workspace/TranskribusCore-0.1.2.jar -DgroupId=eu.transkribus -DartifactId=TranskribusCore -Dversion=0.1.2 -Dpackaging=jar
RUN cd /workspace && mvn clean package -DskipTests

EXPOSE ${CONFIG_SERVER_PORT}

WORKDIR /workspace

ENTRYPOINT ["java","-jar","/workspace/target/ari-transcription-api-0.0.1-SNAPSHOT.jar"]
