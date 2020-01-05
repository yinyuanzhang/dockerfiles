FROM nettworksevtooling/mkfli4l-container:latest
MAINTAINER Florian Wolters <fli4l@florian-wolters.de>

# Configuration for Jenkins swarm

# Default values for potential build time parameters
ARG JENKINS_IP="localhost"
ARG JENKINS_TUNNEL=""
ARG USERNAME="admin"
ARG PASSWORD="admin"
ARG DESCRIPTION="Swarm node with mkfli4l"
ARG LABELS="linux swarm mkfli4l"
ARG NAME="mkfli4l"
ARG UID="1058"
ARG GID="1007"

# Environment variables for swarm client
ENV JENKINS_URL=http://$JENKINS_IP \
    JENKINS_TUNNEL=$JENKINS_TUNNEL \
    JENKINS_USERNAME=$USERNAME \
    JENKINS_PASSWORD=$PASSWORD \
    EXECUTORS=1 \
    DESCRIPTION=$DESCRIPTION \
    LABELS=$LABELS \
    NAME=$NAME \
    SWARM_PLUGIN_VERSION=3.7 \
    WORK_DIR=/data/work \
    SHARED_DIR=/data/shared/fli4l

# Setup jenkins account
# Create working directory
# Change user UID and GID
RUN groupadd --gid ${GID} fleis \
 && useradd --create-home --home-dir /home/jenkins --shell /bin/bash --uid ${UID} --gid ${GID} jenkins \
 && echo "jenkins:jenkins" | chpasswd \
 && chown jenkins:fleis /home/jenkins -R \
 && ulimit -v unlimited

RUN apt-get autoremove \
 && apt-get clean \
 && apt-get update \
 && apt-get install -y \
    default-jdk

# Mount point for Jenkins .ssh folder
VOLUME /home/jenkins/.ssh

# Install swarm client
ADD "https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/${SWARM_PLUGIN_VERSION}/swarm-client-${SWARM_PLUGIN_VERSION}.jar" /data/swarm-client.jar

# Update ownership on /data
RUN chown -R jenkins:fleis /data

# Switch to user jenkins
USER jenkins

CMD java \
    -jar /data/swarm-client.jar \
    -executors "${EXECUTORS}" \
    -noRetryAfterConnected \
    -description "${DESCRIPTION}" \
    -fsroot "${WORK_DIR}" \
    -master "${JENKINS_URL}" \
    -tunnel "${JENKINS_TUNNEL}" \
    -username "${JENKINS_USERNAME}" \
    -password "${JENKINS_PASSWORD}" \
    -labels "${LABELS}" \
    -name "${NAME}" \
-sslFingerprints " "
