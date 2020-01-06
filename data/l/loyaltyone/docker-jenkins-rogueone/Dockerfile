FROM loyaltyone/jenkins-infra:slave-v2.0.3

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8
USER root

RUN apt-get update && apt-get install -y maven

USER root
RUN rm -rf /home/jenkins/build
