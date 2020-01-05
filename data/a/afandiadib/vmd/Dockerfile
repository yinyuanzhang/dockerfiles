FROM centos

MAINTAINER "Adib Afandi bin Abdullah <fendy90.oscura@gmail.com>"

RUN yum install -y perl csh make libXinerama libXi libGL mesa-dri-drivers && \
    curl https://www.ks.uiuc.edu/Research/vmd/vmd-1.9.3/files/final/vmd-1.9.3.bin.LINUXAMD64-CUDA8-OptiX4-OSPRay111p1.opengl.tar.gz -o vmd.tar.gz && \
    tar -xzf vmd.tar.gz && \
    cd vmd-1.9.3 && ./configure LINUXAMD64 && \
    cd src && make install && \
    yum clean all && rm -rf /var/cache/yum/*

CMD vmd
