FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y curl
RUN groupadd -r minecraft && useradd --no-log-init -r -g minecraft minecraft
RUN mkdir -p /home/minecraft && chown minecraft:minecraft /home/minecraft
USER minecraft
WORKDIR /home/minecraft
RUN curl -sL https://get.pmmp.io | bash -s -
