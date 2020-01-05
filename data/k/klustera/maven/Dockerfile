FROM klustera/java8

MAINTAINER Adolfo De Unánue <adolfo@klustera.com>

## Para poder "deploya/compilar" proyectos de Java

ENV MAVEN_VERSION=3.3.3

ENV MAVEN_HOME=/usr/local/maven

ENV PATH $PATH:/usr/bin/mvn

## Instalamos Maven
RUN mkdir -p ${MAVEN_HOME} \
    && curl -sSL -o /Maven-${MAVEN_VERSION}.tar.gz http://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
    && tar zxf /Maven-${MAVEN_VERSION}.tar.gz -C /usr/local \
    && rm -f /Maven-${MAVEN_VERSION}.tar.gz \
    && mv /usr/local/apache-maven-${MAVEN_VERSION}/* ${MAVEN_HOME} \
    && ln -s /usr/local/maven/bin/mvn /usr/bin/mvn \
## Limpiamos
    && rm -fr /usr/local/apache-maven-${MAVEN_VERSION}

CMD ["/usr/bin/mvn"]
