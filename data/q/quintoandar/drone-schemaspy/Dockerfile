# Pull base image
FROM ubuntu:bionic

RUN apt-get update && \
    apt-get upgrade -y && \
    # java 8
    apt-get install openjdk-8-jre -y && \
    # SchemaSpy external dependencies
    apt-get install -y graphviz && \
    # awscli to upload the documentation
    apt-get install -y python-pip && pip install awscli && \
    apt-get clean

ENV JAVA_HOME /usr/bin/java
ENV PATH $PATH:$JAVA_HOME/bin

# Add dependencies to container
COPY /dependencies/mysql-connector-java-5.1.47-bin.jar /dependencies/mysql-connector-java-5.1.47-bin.jar
COPY /dependencies/schemaspy-6.1.0.jar /dependencies/schemaspy-6.1.0.jar
COPY /dependencies/postgresql-42.2.8.jar /dependencies/postgresql-42.2.8.jar
COPY /dependencies/RedshiftJDBC42-no-awssdk-1.2.36.1060.jar /dependencies/RedshiftJDBC42-no-awssdk-1.2.36.1060.jar

COPY entrypoint.sh /bin
ENTRYPOINT /bin/entrypoint.sh
