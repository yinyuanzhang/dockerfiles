FROM adoptopenjdk/openjdk8:latest

RUN apt-get update -y \
    && apt-get install git-core -y

RUN git config --global user.email "dummy@user" \
    && git config --global user.name "dummy user" \
    && git --version