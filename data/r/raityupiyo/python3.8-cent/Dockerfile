FROM centos:7

RUN yum groupinstall -y "development tools" && \
yum install -y bzip2-devel gdbm-devel libffi-devel \
libuuid-devel ncurses-devel openssl-devel readline-devel \
sqlite-devel tk-devel wget xz-devel zlib-devel && \
curl -O https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz && \
tar xf Python-3.8.0.tgz && \
cd Python-3.8.0 && \
./configure && \
make altinstall && \
python3.8 -m pip install --upgrade pip && \
rm -rf /Python-3.8.0 /Python-3.8.0.tgz