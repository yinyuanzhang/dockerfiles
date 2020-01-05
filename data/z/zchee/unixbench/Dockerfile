FROM ubuntu:14.04
MAINTAINER Borja Burgos <borja@tutum.co>
MAINTAINER Takuya Arita <takuya.arita@gmail.com>

# Fix locale errors
RUN export LANG=en_US.UTF-8
RUN export LC_ALL=$LANG
RUN locale-gen --purge $LANG
RUN dpkg-reconfigure -f noninteractive locales && /usr/sbin/update-locale LANG=$LANG LC_ALL=$LANG

# Use a mirror close to me
RUN sed -i s/archive.ubuntu.com/ftp.jaist.ac.jp/ /etc/apt/sources.list

# Install Dependencies
RUN apt-get update && apt-get install -y build-essential libx11-dev libgl1-mesa-dev libxext-dev perl perl-modules

# Download UnixBench
ADD http://byte-unixbench.googlecode.com/files/UnixBench5.1.3.tgz /tmp/UnixBench5.1.3.tgz

# Decompress UnixBench
WORKDIR /tmp
RUN tar -xzf UnixBench5.1.3.tgz

# Run UnixBench
WORKDIR /tmp/UnixBench
RUN make all
ENTRYPOINT ["./Run"]
