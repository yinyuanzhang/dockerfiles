# Base image
FROM openjdk:8-jdk-alpine

# Variables
ARG UID=9999
ARG GID=9999
ENV UID=${UID}
ENV GID=${GID}

# Install ALPINE packages
RUN apk update && apk upgrade && \
    apk add --no-cache shadow bash git openssh curl
    
# Create group and user that will run the gateway
RUN groupadd -r -g ${GID} app && useradd -r -u ${UID} -g app -d /gateway -s /sbin/nologin -c "Image user" app

# Pull repository
RUN git clone https://github.com/vicinityh2020/vicinity-gateway-api.git

# Move files to working dir
RUN mkdir gateway \
    && mkdir gateway/target \
    && mkdir gateway/config \
    && mkdir gateway/keystore \
    && mv vicinity-gateway-api/target/ogwapi-jar-with-dependencies.jar /gateway/target/ \
    && mv vicinity-gateway-api/config/* /gateway/config/ \
    && mv vicinity-gateway-api/keystore/genkeys.sh /gateway/keystore/ \
    && rm -rf vicinity-gateway-api
WORKDIR /gateway

# Change rights and user
RUN chmod 764 ./target/ogwapi-jar-with-dependencies.jar \
    && mkdir ./log/ \
    && chmod -R 777  ./log/ \
    && mkdir ./data/ \
    && chmod -R 777  ./data/ \
    && chown -R app:app /gateway \
    && chmod 764 ./config/GatewayConfig.xml \
    && chmod +x ./keystore/genkeys.sh
USER app

# Select port
EXPOSE  8181

# Start the gateway-api in docker container
CMD ["java", "-jar", "./target/ogwapi-jar-with-dependencies.jar"]
