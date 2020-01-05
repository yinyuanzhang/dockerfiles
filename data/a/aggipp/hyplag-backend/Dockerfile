# Builder image with Maven
FROM maven:3.6-jdk-8-alpine as builder

USER root
WORKDIR /hyplag-build

# source
COPY pds-backend-batch/ ./pds-backend-batch/
COPY pds-backend-converter-grobid/ ./pds-backend-converter-grobid/
COPY pds-backend-converter-jats2tei/ ./pds-backend-converter-jats2tei/
COPY pds-backend-converter-pdf2tei/ ./pds-backend-converter-pdf2tei/
COPY pds-backend-core/ ./pds-backend-core/
COPY pds-backend-util/ ./pds-backend-util/
COPY pom.xml .

RUN mvn clean install -DskipTests


# HyPlag Base Image =========================
FROM openjdk:8-jre-slim
LABEL maintainer="vincent.stange@uni-konstanz.de"

# libxml2 for Grobid, rest for SSH and networking tools
RUN apt-get update \
  && apt-get --no-install-recommends install -y libxml2 \
  && apt-get install -y openssh-server curl vim dnsutils net-tools iputils-ping iproute2 jq build-essential python \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && mkdir /var/run/sshd
# Set up automatic login as root for ssh sessions
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

# Copy SSH keys for this container
RUN mkdir /root/.ssh
COPY ssh_config/authorized_keys /root/.ssh/authorized_keys
# Set permission right and SSH update
RUN chmod 600 /root/.ssh/authorized_keys

WORKDIR /hyplag

# Use local files or Docker build with builder image
COPY --from=builder /hyplag-build/pds-backend-core/target/pds-backend-core-*.jar backend.jar
COPY --from=builder /hyplag-build/pds-backend-batch/target/pds-backend-batch-*.jar batch.jar
#COPY /pds-backend-core/target/pds-backend-core-*.jar backend.jar
#COPY /pds-backend-batch/target/pds-backend-batch-*.jar batch.jar

# Copy Configuration and Grobid Home dependency
COPY /pds-backend-core/src/main/resources/config/application.docker.yaml application.yaml
COPY /hyplag-grobid/grobid-home grobid-home
COPY /pds-backend-core/lib lib

# Java 8 and 9 ignore container restriction, UnlockExperimentalVMOptions and UseCGroupMemoryLimitForHeap
# will limit the heap, see https://developers.redhat.com/blog/2017/04/04/openjdk-and-containers/#more-433899
# ENV JAVA_OPTS="-XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap"

EXPOSE 8080

# Run SSH and the application
CMD /usr/sbin/sshd -E /var/log/ssh.log &&\
 java\
 -XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap -Xdebug -agentlib:jdwp=transport=dt_socket,address=50505,server=y,suspend=n\
 -Xms1G -Xmx8G\
 -jar backend.jar\
 --spring.config.location=file:application.yaml
# CMD ["java", "-XX:+UnlockExperimentalVMOptions", "-XX:+UseCGroupMemoryLimitForHeap", "-jar","backend.jar", "--spring.config.location=file:application.yaml"]
