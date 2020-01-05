# The only assumption we make about this FROM is that it has a JRE in path
FROM solsson/kafka-jre@sha256:06dabfc8cacd0687c8f52c52afd650444fb6d4a8e0b85f68557e6e7a5c71667c

## CREATE APP USER ##
####################################################################
####################################################################
####################################################################

# Create the home directory for the new app user.
RUN mkdir -p /opt/kafka

# Set the home directory to our app user's home.
ENV APP_HOME=/opt/kafka

# Create an app user so our program doesn't run as root.
RUN groupadd -r app &&\
    useradd -r -g app -d /opt/kafka -s /sbin/nologin -c "Docker image user" app
    
# Chown all the files to the app user.
RUN chown -R app:app $APP_HOME

## SETTING UP THE APP ##
WORKDIR $APP_HOME

####################################################################
####################################################################
####################################################################


ENV KAFKA_VERSION=1.0.0 SCALA_VERSION=2.11

RUN set -ex; \
  export DEBIAN_FRONTEND=noninteractive; \
  runDeps='netcat-openbsd'; \
  buildDeps='curl ca-certificates'; \
  apt-get update && apt-get install -y $runDeps $buildDeps --no-install-recommends; \
  \
  SCALA_BINARY_VERSION=$(echo $SCALA_VERSION | cut -f 1-2 -d '.'); \
  
  curl -SLs "https://www-eu.apache.org/dist/kafka/$KAFKA_VERSION/kafka_$SCALA_BINARY_VERSION-$KAFKA_VERSION.tgz" | tar -xzf - --strip-components=1 -C /opt/kafka; \
  \
  rm -rf /opt/kafka/site-docs; \
  \
  apt-get purge -y --auto-remove $buildDeps; \
  rm -rf /var/lib/apt/lists/*; \
  rm -rf /var/log/dpkg.log /var/log/alternatives.log /var/log/apt; \
  
####################################################################
####################################################################
####################################################################

# Change to the app user.
USER app
