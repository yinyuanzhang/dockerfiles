FROM guptasanchit90/klybasebuildimage as build-image

ENV BRANCH=release/0.9.1

# Checkout kylo
RUN mkdir -p /usr/local/src/ && cd /usr/local/src/ && git clone --branch $BRANCH https://github.com/Teradata/kylo.git

# Compile 
RUN cd /usr/local/src/kylo/ && /usr/local/src/apache-maven/bin/mvn package -B -DskipTests=true -Dlicense.skipCheckLicense=true -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn

# Copy tar to another location
RUN mkdir -p /opt/kylo && mv /usr/local/src/kylo/install/install-tar/target/kylo-*-dependencies.tar.gz /opt/kylo/

FROM alpine
RUN mkdir -p /opt/kylo
COPY --from=build-image /opt/kylo/ /opt/kylo
