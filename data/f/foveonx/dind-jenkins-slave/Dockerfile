FROM jenkins/ssh-slave
RUN  curl -sSL https://get.docker.com/ | sh
RUN apt-get update &&\
    apt-get install -y openjdk-8-jdk &&\
    apt-get clean -y && rm -rf /var/lib/apt/lists/*
COPY /home/user/dockerfile/Dockerfile/http-server/Dockerfile /home/user/dockerfile/Dockerfile/http-server/Dockerfile

