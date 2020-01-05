# Build jar with gradle:
# NOTICe: previously the gradle build was used to create the docker container. 
# Now this Dockerfile uses gradle to build the application, and then the container.
# The old Dockerfile generatede by gradle is found in the "build/" directory and will be removed in an upcoming commit.

FROM gradle:jdk11 as builder
COPY --chown=gradle:gradle . /home/gradle/src
WORKDIR /home/gradle/src
RUN gradle build --stacktrace


# creates an image from executable jar built with gradle

FROM openjdk:11-jre-slim
LABEL maintainer="cstool_io@koderman.de"

EXPOSE 8080
COPY --from=builder /home/gradle/src/build/libs/cveservice.jar /app/

ENTRYPOINT java -jar /app/cveservice.jar

# set the following environment variables when running:
# i.e. docker run -e mongo.port=8080 -e mongo.host=cve-mongo akoderman/cveservice:latest

#--mongo.port=8080 \
#--mongo.host=cve-mongo \
#--mongo.user=akoderman \
#--mongo.password=secret \
#--mongo.protocol=mongo+srv \
#--mongo.database=cvedb








