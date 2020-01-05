FROM jenkins/jnlp-slave:3.26-1

USER root
RUN apt update && apt install build-essential -y
USER jenkins

ENTRYPOINT ["jenkins-slave"]
