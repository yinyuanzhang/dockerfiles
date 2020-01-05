FROM isuper/base-ubuntu

ENV VERSION 8
ENV UPDATE 131
ENV BUILD 11

ENV JAVA_HOME /usr/lib/jvm/java-${VERSION}-oracle
ENV JRE_HOME ${JAVA_HOME}/jre

ENV MAVEN_VERSION=3.0.5
ENV MAVEN_HOME=/opt/mvn

# change to tmp folder
WORKDIR /tmp

# Exemple d'URL pour récupérer le jdk java oracle
# http://download.oracle.com/otn-pub/java/jdk/8u101-b13/jdk-8u101-linux-x64.tar.gz

RUN apt-get update && apt-get install ca-certificates curl wget -y --no-install-recommends
RUN curl --silent --location --retry 3 --cacert /etc/ssl/certs/GeoTrust_Global_CA.pem --header "Cookie: oraclelicense=accept-securebackup-cookie;" http://download.oracle.com/otn-pub/java/jdk/"${VERSION}"u"${UPDATE}"-b"${BUILD}"/jdk-"${VERSION}"u"${UPDATE}"-linux-x64.tar.gz	| tar xz -C /tmp
RUN mkdir -p /usr/lib/jvm && mv /tmp/jdk1.${VERSION}.0_${UPDATE} "${JAVA_HOME}"
RUN apt-get remove --purge --auto-remove -y
RUN apt-get autoclean && apt-get --purge -y autoremove
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN update-alternatives --install "/usr/bin/java" "java" "${JRE_HOME}/bin/java" 1 && \
	update-alternatives --install "/usr/bin/javac" "javac" "${JAVA_HOME}/bin/javac" 1 && \
	update-alternatives --set java "${JRE_HOME}/bin/java" && \
	update-alternatives --set javac "${JAVA_HOME}/bin/javac"

# Download and extract maven to opt folder
RUN wget --no-check-certificate --no-cookies http://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
    && wget --no-check-certificate --no-cookies http://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz.md5 \
    && echo "$(cat apache-maven-${MAVEN_VERSION}-bin.tar.gz.md5) apache-maven-${MAVEN_VERSION}-bin.tar.gz" | md5sum -c \
    && tar -zvxf apache-maven-${MAVEN_VERSION}-bin.tar.gz -C /opt/ \
    && ln -s /opt/apache-maven-${MAVEN_VERSION} /opt/mvn \
    && rm -f apache-maven-${MAVEN_VERSION}-bin.tar.gz \
    && rm -f apache-maven-${MAVEN_VERSION}-bin.tar.gz.md5

# add executables to path
RUN update-alternatives --install "/usr/bin/mvn" "mvn" "/opt/mvn/bin/mvn" 1 && \
    update-alternatives --set "mvn" "/opt/mvn/bin/mvn"

# change to root folder
WORKDIR /root
