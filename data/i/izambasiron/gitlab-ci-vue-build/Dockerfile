FROM node:6

RUN apt-get update -y && apt-get install openssh-client -y
RUN eval $(ssh-agent -s)
RUN mkdir -p ~/.ssh
RUN chmod 700 ~/.ssh