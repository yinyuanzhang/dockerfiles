FROM debian:latest
RUN apt-get update
RUN mkdir -p /root/.local/share
RUN apt-get install -y \
    inkscape \
    pstoedit \
    openscad \
    meshlab \
    xvfb \
    build-essential \
    curl \
    unzip
WORKDIR /buddy
CMD make
