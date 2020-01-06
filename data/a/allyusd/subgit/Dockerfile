FROM openjdk:8-jre

RUN apt-get update && apt-get install curl subversion git -y

RUN curl -O https://subgit.com/files/subgit-3.3.5.zip && unzip subgit-3.3.5.zip && cd subgit-3.3.5/bin/

WORKDIR /subgit-3.3.5/bin
