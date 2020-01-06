# Centos 6 with python 3.6 from scl and Pyinstaller ready 
FROM centos:6 

RUN yum makecache fast && yum install -y centos-release-scl-rh && yum install -y rh-python36 xz && yum clean all
COPY source_rh-python36.sh /etc/profile.d/source_rh-python36.sh
RUN ln -s /opt/rh/rh-python36/root/usr/lib64/libpython3.6m.so.rh-python36-1.0 /opt/rh/rh-python36/root/usr/lib64/libpython3.6m.so.1.0 
RUN source /opt/rh/rh-python36/enable && pip3 install --upgrade pip && pip3 install PyInstaller
RUN curl -L  https://github.com/upx/upx/releases/download/v3.94/upx-3.94-amd64_linux.tar.xz | tar -xJ -C /opt/

ENTRYPOINT ["scl", "enable", "rh-python36", "--", "bash", "-c"]
