FROM balenalib/raspberry-pi
RUN ["cross-build-start"]
RUN apt-get update && \ 
    apt-get -y upgrade && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /mnt
RUN ["cross-build-end"]
