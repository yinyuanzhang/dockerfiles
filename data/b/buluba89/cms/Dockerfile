#-------------- Build ---------------
FROM maven:3-jdk-8 as build

# Add all poms to cache dependencies
ADD ./pom.xml /build/pom.xml
ADD ./common/pom.xml /build/common/pom.xml
ADD ./common/api/pom.xml /build/common/api/pom.xml
ADD ./common/client/pom.xml /build/common/client/pom.xml
ADD ./common/dataobjects/pom.xml /build/common/dataobjects/pom.xml
ADD ./common/services/pom.xml /build/common/services/pom.xml
ADD ./server/pom.xml /build/server/pom.xml
ADD ./client/pom.xml /build/client/pom.xml
ADD ./integration-tests/pom.xml /build/integration-tests/pom.xml
# Download dependencies
RUN cd /build && mvn verify clean --fail-never

# Add all and build
ADD . /build
RUN cd /build  && mvn install -DskipTests

#------------- Run env --------------
FROM java:openjdk-8-jdk-alpine as webapp

# Define enviroment variables
ENV JAVA_XMX=256m
ENV SASTIX_CMS_SERVER_PORT=9082

COPY --from=build /build/server/target/cms-server-*.jar /app.jar

WORKDIR /opt/csp
RUN mkdir -p /opt/sastixcms

EXPOSE 9082

CMD java \
    -Xmx$JAVA_XMX \
    $JAVA_EXTRA_ARGS \
    -jar /app.jar