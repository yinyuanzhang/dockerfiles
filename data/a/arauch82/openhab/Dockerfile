FROM openhab/openhab:latest
MAINTAINER Andreas Rauch <mail@andreas-rauch.de>

# install openssh client
RUN apt-get update && apt-get install -y \
        openssh-client \
        librxtx-java \
        && rm -rf /var/lib/apt/lists/*
