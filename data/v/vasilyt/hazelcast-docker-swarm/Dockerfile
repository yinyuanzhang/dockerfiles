FROM openjdk:8u171-jre-alpine
LABEL authors="Pavel <pavel@multiloginapp.com>, Igor <igorzep@gmail.com>"

# Versions of Hazelcast and Hazelcast plugins
ARG HZ_VERSION=3.10.6
ARG CACHE_API_VERSION=1.0.0
ARG HZ_SWARM_VERSION=1.0-RC8

# Build constants
ARG HZ_HOME="/opt/hazelcast"
ARG HZ_JAR="hazelcast-all-${HZ_VERSION}.jar"
ARG CACHE_API_JAR="cache-api-${CACHE_API_VERSION}.jar"

# Install bash & curl
RUN apk add --no-cache bash curl \
 && rm -rf /var/cache/apk/*

# Set up build directory
RUN mkdir -p ${HZ_HOME}
WORKDIR ${HZ_HOME}

# Download & install Hazelcast
RUN curl -svf -o ${HZ_HOME}/${HZ_JAR} \
         -L https://repo1.maven.org/maven2/com/hazelcast/hazelcast-all/${HZ_VERSION}/${HZ_JAR}

# Download & install JCache
RUN curl -svf -o ${HZ_HOME}/${CACHE_API_JAR} \
         -L https://repo1.maven.org/maven2/javax/cache/cache-api/${CACHE_API_VERSION}/${CACHE_API_JAR}

# Download and install Hazelcast plugins (hazelcast-swarm) with dependencies
RUN curl -svf -o ${HZ_HOME}/hazelcast-docker-swarm-discovery-spi.jar \
         -L http://repo.spring.io/plugins-release/org/bitsofinfo/hazelcast-docker-swarm-discovery-spi/${HZ_SWARM_VERSION}/hazelcast-docker-swarm-discovery-spi-${HZ_SWARM_VERSION}.jar

# Set Pardot ID to 'docker'
RUN echo 'hazelcastDownloadId=docker' > hazelcast-download.properties

# Runtime constants
ENV CLASSPATH_DEFAULT "${HZ_HOME}:${HZ_HOME}/*"
ENV JAVA_OPTS_DEFAULT "-Djava.net.preferIPv4Stack=true"

# Runtime environment variables
ENV MIN_HEAP_SIZE ""
ENV MAX_HEAP_SIZE ""
ENV CLASSPATH ""
ENV JAVA_OPTS ""

### Expose port
EXPOSE 5701

# Start Hazelcast server
CMD ["bash", "-c", "set -euo pipefail \
      && if [[ \"x${CLASSPATH}\" != \"x\" ]]; then export CLASSPATH=\"${CLASSPATH_DEFAULT}:${CLASSPATH}\"; else export CLASSPATH=\"${CLASSPATH_DEFAULT}\"; fi \
      && if [[ \"x${JAVA_OPTS}\" != \"x\" ]]; then export JAVA_OPTS=\"${JAVA_OPTS_DEFAULT} ${JAVA_OPTS}\"; else export JAVA_OPTS=\"${JAVA_OPTS_DEFAULT}\"; fi \
      && if [[ \"x${MIN_HEAP_SIZE}\" != \"x\" ]]; then export JAVA_OPTS=\"${JAVA_OPTS} -Xms${MIN_HEAP_SIZE}\"; fi \
      && if [[ \"x${MAX_HEAP_SIZE}\" != \"x\" ]]; then export JAVA_OPTS=\"${JAVA_OPTS} -Xmx${MAX_HEAP_SIZE}\"; fi \
      && echo \"########################################\" \
      && echo \"# JAVA_OPTS=${JAVA_OPTS}\" \
      && echo \"# CLASSPATH=${CLASSPATH}\" \
      && echo \"# starting now....\" \
      && echo \"########################################\" \
      && set -x \
      && exec java -server ${JAVA_OPTS} com.hazelcast.core.server.StartServer \
     "]     
