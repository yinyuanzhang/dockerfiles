FROM centos:7.2.1511
LABEL name="dtl-base"
LABEL maintainer="cjiang<jch.cst@gmail.com>"

COPY resource /tmp/resource
# 时区设置
ENV TZ=Asia/Shanghai
# 初始化 /etc/machine-id
RUN systemd-machine-id-setup && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    echo "install traderslink env" && \
    echo -e "\\033[45;37m ############### yum ############### \033[0m" && \
    yum -y install deltarpm epel-release && \
    yum -y install python-devel python-pip && \
    yum -y install make gcc gcc-c++ vim net-tools telnet tcpdump sysstat which wget git && \
    yum -y install bzip2-devel zlib-devel openssl-devel rpm-build && \
    yum -y install gtest gtest-devel && \
    echo -e "\\033[45;37m ############### yum local ############### \033[0m" && \
    cd /tmp/resource/ && yum install mysql80-community-release-el7-1.noarch.rpm -y && yum --enablerepo=mysql-connectors-community install mysql-connector-c++-devel -y && \
    cd /tmp/resource/ && wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.6.0-x86_64.rpm && yum install filebeat-6.6.0-x86_64.rpm -y && \
    echo -e "\\033[45;37m ############### boost / cmake ############### \033[0m" && \
    cd /tmp/resource/ && wget https://dl.bintray.com/boostorg/release/1.69.0/source/boost_1_69_0.tar.gz && tar -xvf boost_1_69_0.tar.gz && cd boost_1_69_0 && ./bootstrap.sh && ./b2 install -j2 && \
    cd /tmp/resource/ && wget https://github.com/Kitware/CMake/releases/download/v3.13.3/cmake-3.13.3.tar.gz && tar -xvf cmake-3.13.3.tar.gz && cd cmake-3.13.3 && ./bootstrap && make install -j4 && \
    echo -e "\\033[45;37m ############### source code ############### \033[0m" && \
    cd /tmp/resource/ && git clone git://github.com/zeromq/libzmq.git && cd libzmq && git checkout tags/v4.3.1 && mkdir build && cd build && cmake .. -DBUILD_TESTS=OFF && make install -j4 && \
    cd /tmp/resource/ && git clone git://github.com/pybind/pybind11.git && cd pybind11 && git checkout tags/v2.2.4 && mkdir build && cd build && cmake .. -DPYBIND11_TEST=OFF && make install -j4 && \
    cd /tmp/resource/ && git clone git://github.com/nanomsg/nanomsg.git && cd nanomsg && git checkout tags/1.1.5 && mkdir build && cd build && cmake .. -DNN_TESTS=OFF && make install -j4 && \
    yum -y clean all && rm -rf /tmp/resource

WORKDIR /shared/
