# Gedco Ubuntu 18.04 + AWS Corretto JDK8 + Maven 3.5.4 base dev/prod Docker image.
#
# Build usage: docker build -t gedco:ubuntu-java --pull --rm .
#   Run usage: docker run --name java-example --rm -d -it -v $(pwd)/src:/usr/src/ gedco:ubuntu-java /bin/bash
#        Stop: docker stop java-example
#
# See Correto Releases here: https://github.com/corretto/corretto-8/releases
FROM ubuntu:18.04

# Mark this system as noninteractive.
ENV DEBIAN_FRONTEND noninteractive
ENV MAVEN_VERSION 3.6.2
ENV PATH /opt/apache-maven-${MAVEN_VERSION}/bin:${PATH}
ENV CORRETTO_URL https://d3pxv6yz143wms.cloudfront.net/8.232.09.1/java-1.8.0-amazon-corretto-jdk_8.232.09-1_amd64.deb
ENV MAVEN_URL http://www.eu.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz

# Install and configure all the software. Clean.
RUN apt-get update -qq; apt-get --yes upgrade -qq; \
    apt-get install --yes java-common wget less nano -qq; \
    wget ${CORRETTO_URL} -O /tmp/corretto.deb --quiet; dpkg -i /tmp/corretto.deb; \
    cd /opt/; wget ${MAVEN_URL} -O maven.tar.gz --quiet; tar -xzf maven.tar.gz; \
    echo "------------ DONE -------------"; java -version; mvn -version; \
    rm -rf /tmp/*.deb; rm -rf /opt/*.tar.gz; apt-get clean;

# Default bash command.
CMD ["/bin/bash"]
