FROM maven:3.6-jdk-8 as build
WORKDIR /build

# Fetch deps als eigener Schritt, kann Docker dann cachen
COPY pom.xml /build
RUN mvn verify clean --fail-never

# Copy source und Build
COPY src /build/src
RUN mvn clean install -Dmaven.test.skip=true

# Runtime image
FROM openjdk:8-jdk as runtime

# Add Tini
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

# Guteberg
WORKDIR /application

COPY --from=build /build/target/gutenberg-reloaded*.jar /application/target/
COPY src/main/resources /application/src/main/resources

CMD ["java", "-XX:+UnlockExperimentalVMOptions", "-XX:+UseCGroupMemoryLimitForHeap", "-jar", "/application/target/gutenberg-reloaded.jar"]

EXPOSE 5000
