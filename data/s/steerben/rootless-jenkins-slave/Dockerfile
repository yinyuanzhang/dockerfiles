FROM jenkins/jnlp-slave:latest

MAINTAINER Benjamin Steer <benjamin.steer@gmail.com>
LABEL Description="This is an image based on jenkins/jnlp-slave running with non root user id"

USER 10000

ENTRYPOINT ["jenkins-slave"]
