FROM centos:7

COPY bashrc /root/.bashrc

RUN yum install -y which \ 
 wget gcc-c++ libSM libXext libXpm libXft libpng libjpeg qt \
 && cd \
 && wget https://root.cern.ch/download/root_v6.08.00.Linux-centos7-x86_64-gcc4.8.tar.gz \
 && tar -zvxf root_v6.08.00.Linux-centos7-x86_64-gcc4.8.tar.gz \
 && rm root_v6.08.00.Linux-centos7-x86_64-gcc4.8.tar.gz

