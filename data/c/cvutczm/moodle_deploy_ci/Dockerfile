
FROM debian:jessie-slim

RUN apt-get update -y
RUN apt-get install openssh-client -y
RUN apt-get install dos2unix -y
RUN mkdir -p ~/.ssh
RUN eval $(ssh-agent -s)
RUN echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config
