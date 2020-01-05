FROM centos

# Install Dependencies
RUN yum -y update && yum -y groupinstall "Development Tools" && yum -y install perl perl-Time-HiRes

# Download UnixBench
ADD http://byte-unixbench.googlecode.com/files/UnixBench5.1.3.tgz /tmp/UnixBench5.1.3.tgz

# Decompress UnixBench
WORKDIR /tmp
RUN tar -xzf UnixBench5.1.3.tgz

# Run UnixBench
WORKDIR /tmp/UnixBench
RUN make all
ENTRYPOINT ["./Run"]
