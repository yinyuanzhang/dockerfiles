FROM zombiefeynman/manylinux2010_x86_64

RUN wget -q https://github.com/Kitware/CMake/releases/download/v3.13.3/cmake-3.13.3.tar.gz \
 && tar xf cmake-3.13.3.tar.gz \
 && cd cmake-3.13.3 \
 && ./bootstrap \
 && make \
 && make install \
 && cd .. \
 && rm -rf cmake-3.13.3.tar.gz \
           cmake-3.13.3

RUN yum -y update \
 && yum install -y https://centos6.iuscommunity.org/ius-release.rpm \
 && yum -y install python36* \
 && rm -rf /var/cache/yum/* \
 && yum clean all
