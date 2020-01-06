FROM centos:7
MAINTAINER Dave Luo <kitsudo163@163.com>
RUN rpmdb --rebuilddb && yum install -y nc htop net-tools telnet wget tcpdump && yum clean all
RUN /bin/cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN rpmdb --rebuilddb && yum install -y \
    curl \
    wget \
    tar \
    gcc \
    zlib-devel \
    openssl \
    openssl-devel \ 
    bzip2-devel \
    git \
    libffi-devel \
    && \
    yum clean all && \
    echo "[Prepare]"

RUN cd /tmp && \
    wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz && \
    tar xfz Python-3.6.8.tgz && \
    cd Python-3.6.8 && \
    ./configure --prefix=/usr/local && \
    make && \
    make altinstall && \
    echo "[Python]"
# RUN curl -LS "https://bootstrap.pypa.io/get-pip.py" | python2.7 && \
#    echo "[pip]"
RUN cd /tmp && \
    wget http://mirrors.aliyun.com/pypi/packages/6b/dd/a7de8caeeffab76bacf56972b3f090c12e0ae6932245abbce706690a6436/setuptools-28.3.0.tar.gz && \
    tar -zxvf setuptools-28.3.0.tar.gz && \
    cd setuptools-28.3.0 && \
    python3.6 setup.py install && \
    wget http://mirrors.aliyun.com/pypi/packages/e7/a8/7556133689add8d1a54c0b14aeff0acb03c64707ce100ecd53934da1aa13/pip-8.1.2.tar.gz && \
    tar -xzvf pip-8.1.2.tar.gz && \
    cd pip-8.1.2 && \
    python3.6 setup.py install && \
    echo "[pip]"

# zeroc-ice
RUN wget https://zeroc.com/download/Ice/3.7/el7/zeroc-ice3.7.repo -O /etc/yum.repos.d/zeroc-ice3.7.repo && rpmdb --rebuilddb && yum install -y gcc-c++ ice-all-runtime ice-all-devel && yum clean all && pip3.6 install zeroc-ice --trusted-host mirrors.aliyun.com -i http://mirrors.aliyun.com/pypi/simple

RUN pip3.6 install pipenv

ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
RUN curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
