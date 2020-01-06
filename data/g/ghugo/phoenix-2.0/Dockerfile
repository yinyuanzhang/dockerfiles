FROM debian:stable

MAINTAINER Hugo Guiroux <gx.hugo@gmail.com> version: 0.1

# Install tools to build
RUN apt-get update && apt-get install -y \
  build-essential \
  git \
  wget && \
  rm -rf /var/lib/apt/lists/*

# Clone the repository of the original author
RUN git clone https://github.com/kozyraki/phoenix.git

# Compile phoenix
RUN cd phoenix/phoenix-2.0 && make

# Copy the list of datasets inside the container
COPY datasets_list.txt /tmp/

# Retrieve the datasets
RUN mkdir -p /data && \
    cd /data && \
    wget -i /tmp/datasets_list.txt && \
	for f in *.tar.gz; do tar -xf $f && rm $f; done

