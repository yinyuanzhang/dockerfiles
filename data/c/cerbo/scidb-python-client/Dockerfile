FROM ubuntu:latest
MAINTAINER Cerbo IO <support@cerbo.io>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update ; \
apt-get -y install perl python3 ipython3 python3-pip libopenjpeg-dev python3-grib python3-netcdf4 python3-pandas openssh-server wget git screen vim-nox emacs-nox ; \
ln -s /usr/bin/python3 /usr/local/bin/python ; \
pip3 install --upgrade pip ;\
pip3 install scidb-py ; \
pip3 install jupyter ; \
git clone https://github.com/facebook/zstd.git ; \
cd zstd ; \
make && make install ; \
cd ../ && rm -Rf zstd ; \
sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config ; \
echo "root:scidb" | chpasswd ; \
mkdir -p /usr/local/scidb/bin /usr/local/scidb/lib ; \
mkdir -p /opt/scidb/15.12/3rdparty/cityhash/lib/ ; \
echo "export PATH=/usr/local/scidb/bin:$PATH" >> /root/.bashrc

COPY iquery /usr/local/scidb/bin/
COPY usr-local-scidb-lib/* /usr/local/scidb/lib/
COPY lib-x86_64-linux-gnu/* /lib/x86_64-linux-gnu/
COPY libcityhash.so.0 /opt/scidb/15.12/3rdparty/cityhash/lib/
COPY start-ssh /

EXPOSE 22
CMD ["/bin/bash"]
