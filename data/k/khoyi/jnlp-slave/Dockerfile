# Place in docker container, use jenkins, or jenkins controlled docker container...

# Base image
FROM jenkins/jnlp-slave
# Going god-mode
USER root

# Python 3 w/ PyYaml
RUN \
  apt update && \
  apt -y install python3 python3-pip && \
  pip3 install pyyaml

# Mountable Directories
VOLUME ["/srv/masters", "/srv/plex"]

# drop back to the regular jenkins user - good practice
USER jenkins
