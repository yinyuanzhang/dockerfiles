FROM maven:3.5.2-jdk-8

# Install Deps
RUN apt-get update && \
  apt-get install -y --force-yes rpm expect

# Cleaning
RUN apt-get clean

ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000

# If you bind mount a volume from the host or a data container,
# ensure you use the same uid
RUN groupadd -g ${gid} ${group} \
&& useradd -d "/home/jenkins" -u ${uid} -g ${gid} -m -s /bin/bash ${user}
