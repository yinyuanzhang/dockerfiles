FROM centos:7.0.1406
MAINTAINER for cocos2dx <kitsudo163@163.com>
COPY sdk /opt/sdk
RUN yum install -y ant-apache-regexp glibc.i686 libstdc++ libstdc++.i686 \
    && yum install -y zlib.i686 --setopt=protected_multilib=false \
    && yum clean all
ENV PATH=/opt/sdk/tools:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
COPY cocos2d-x-3.5 /opt/cocos2d-x-3.5
ENV NDK_ROOT=/opt/sdk/android-ndk-r10e ANDROID_SDK_ROOT=/opt/sdk
RUN cd /opt/cocos2d-x-3.5 && python setup.py
CMD bash