FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# Install cron
RUN apt-get update && apt-get install -y cron git curl moreutils tzdata

RUN mkdir minecraft && \
    cd minecraft && \
    git clone https://github.com/krimil/minecraft-bedrock-server.git

# Add files
ADD update.sh /minecraft/update.sh
ADD entrypoint.sh /entrypoint.sh
 
RUN chmod +x /minecraft/update.sh /entrypoint.sh

WORKDIR /minecraft
ENTRYPOINT /entrypoint.sh
