FROM jenkinsci/slave:latest
USER root
RUN apt-get update \
    && apt-get install -y python-dev python-pip libssl-dev \
    && pip install ansible
USER jenkins
