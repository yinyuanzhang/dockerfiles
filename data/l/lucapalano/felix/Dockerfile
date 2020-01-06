FROM centos:7
MAINTAINER "Luca Palano" <contact@lpzone.it>
LABEL releaseDate="29-09-2017"

# Env setup
RUN yum update -y && yum install java-1.8.0-openjdk.x86_64 -y
WORKDIR /home/felix

# Download of felix 5.6.8 from official repo
ADD https://archive.apache.org/dist/felix/org.apache.felix.main.distribution-5.6.8.tar.gz ./apache-felix-5.6.8.tar.gz

RUN tar xvfz apache-felix-5.6.8.tar.gz && rm apache-felix-5.6.8.tar.gz

CMD FELIX_FRAMEWORK_PATH=$(printf %s $PWD/$(ls -1)) && cd ${FELIX_FRAMEWORK_PATH} && java -jar ./bin/felix.jar
