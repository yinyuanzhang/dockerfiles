# 1 - Define base image
FROM ubuntu:16.04

# 2 - Set environment to be noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# 3 - Configure apt to not require confirmation (assume the -y argument by default)
RUN echo "APT::Get::Assume-Yes \"true\";" > /etc/apt/apt.conf.d/90assumeyes

# 4 - Run apt update
RUN apt-get update

# 5 - Install all needed packages
RUN apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        jq \
        git \
        iputils-ping \
        libcurl3 \
        libicu55 \
        libunwind8 \
        netcat \
        wget \
        dpkg \
        docker.io

# 6 - Change working directory to /azp
WORKDIR /azp

# 7 - Copy the start script to the docker container
COPY ./start.sh .

# 8 - Make the start script executable
RUN chmod +x start.sh

# 9 - Download Google Chrome debian package
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# 10 - Install downloaded Google Chrome debian package
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# 11 - Execute start script
CMD ["./start.sh"]
