FROM groovy:2.5.2-jdk8

USER root

RUN apt-get update -y \
    && apt-get install git-core -y

USER groovy

RUN git config --global user.email "Dummy@User" \
    && git config --global user.name "Dummy User"
