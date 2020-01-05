FROM centos:7.4.1708

LABEL MAINTAINER="Vinay Kumar Tiwari vinayxbox@gmail.com"

#Installing Developement tools 
RUN yum -y update \
&& yum group -y install "Development Tools" \
&& yum -y install centos-release-scl-rh \
&& yum -y --enablerepo=centos-sclo-rh-testing install devtoolset-7-gcc devtoolset-7-gcc-c++ \
&& scl enable devtoolset-7 bash \
&& yum -y install botan wget clucene09-core glx-utils mesa-libGLES \
gstreamer-plugins-base libX11 libXrender libXi libXfixes libXext libxslt qt-x11 \
libxkbcommon libxcb xcb-util-image xcb-util-keysyms xcb-util-renderutil \
xcb-util-wm freetype fontconfig git epel-release \
&& yum -y install mosquitto \
&& rm -rf /var/cache/yum \
&& wget http://download.qt.io/official_releases/online_installers/qt-unified-linux-x64-online.run -P /home/ \
&& chmod +x /home/qt-unified-linux-x64-online.run

ENTRYPOINT /bin/bash



