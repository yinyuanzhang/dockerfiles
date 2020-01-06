FROM ubuntu:eoan

WORKDIR /tmp

# set ports
# EXPOSE 8624

# update apt and install dependencies
RUN \
apt-get update -y && \ 
apt-get install -y --no-install-recommends \ 
wget \
openssl \
net-tools \ 
libpython2.7 \ 
python-setuptools \ 
python-minimal \ 
python-pkg-resources \ 
python-m2crypto \ 
python-apsw \ 
python-lxml \  
python-libxslt1 && \

#acestream
mkdir -p /opt/acestream && \
wget -o - http://acestream.org/downloads/linux/acestream_3.1.49_ubuntu_18.04_x86_64.tar.gz && \
tar -zxvf acestream_3.1.49_ubuntu_18.04_x86_64.tar.gz -C /opt/acestream && \
cp -Rnv /usr/lib/x86_64-linux-gnu/* /opt/acestream/lib/ && \

# clean up
apt-get clean && \
apt autoremove -y && \
rm -rf /tmp/* /opt/acestream/data/plugins/*

# add local files
COPY root/ /
RUN chmod +x /opt/start.sh

WORKDIR /
