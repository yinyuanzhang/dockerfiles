FROM node:stretch

# https://github.com/ether/etherpad-lite#user-content-gnulinux-and-other-unix-like-systems
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    gzip \
    libssl-dev \
    pkg-config \
    python

WORKDIR /opt

RUN git clone git://github.com/ether/etherpad-lite.git

WORKDIR /opt/etherpad-lite

RUN bin/installDeps.sh

EXPOSE 9001

CMD ["bin/run.sh", "--root"]
