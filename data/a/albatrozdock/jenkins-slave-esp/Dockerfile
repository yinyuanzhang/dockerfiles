FROM jenkinsci/jnlp-slave:latest

USER root
RUN apt update \
  && apt install make -y \
  && rm -rf /var/lib/apt/lists/*

USER jenkins
