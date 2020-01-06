FROM sgrio/java-oracle:server_jre_8
RUN mkdir -p /aam-api-server/
ADD . /aam-api-server/
WORKDIR /aam-api-server/
RUN ls -la
RUN ./gradlew build
#
FROM sgrio/java-oracle:server_jre_8

RUN apt-get update && apt-get install -y nginx wget

## Executable jar
#RUN mkdir -p /app
##ADD build/libs/aam-api-server-0.0.1-SNAPSHOT.jar /opt/aam-api-server/
## Copy artifact from first image to app dir
COPY --from=0 /aam-api-server/build/libs/aam-api-server-0.0.1-SNAPSHOT.jar /app

#COPY build/libs/aam-api-server-0.0.1-SNAPSHOT.jar /app

# Starter
ADD docker/start.sh /opt/start.sh
RUN chmod +x /opt/start.sh

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Exposed ports.
EXPOSE 8080

# Run from /opt
CMD [ "/opt/start.sh" ]
