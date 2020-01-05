FROM centos:centos6

MAINTAINER Yaniv Aran-Shamir <yaniv@t-y.co>

# Install yum dependencies
RUN yum update -y  && yum install -y \
    nano \
    csh \
    libXp \
    libXmu \
    libXpm \
    libXi \
    libtiff \
    libXinerama \
    elfutils \
    gcc \
    gstreamer-plugins-base.x86_64 \
    gamin \
    mesa-utils \
    mesa-libGL-devel \
    tcsh \
    xorg-x11-server-Xorg \
    xorg-x11-server-Xvfb \
    bzip2-devel \
    git \
    hostname \
    openssl \
    openssl-devel \
    sqlite-devel \
    sudo \
    tar \
    wget \
    zlib-dev && \
    yum groupinstall -y "X Window System" && \
     yum clean all
# Install python2.7
RUN cd /tmp && \
    wget https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz && \
    tar xvfz Python-2.7.8.tgz && \
    cd Python-2.7.8 && \
    ./configure --prefix=/usr/local && \
    make && \
    make altinstall

# Install setuptools + pip
RUN cd /tmp && \
    wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz && \
    tar -xvf setuptools-1.4.2.tar.gz && \
    cd setuptools-1.4.2 && \
    python2.7 setup.py install && \
    curl https://bootstrap.pypa.io/get-pip.py | python2.7 - && \
    pip install virtualenv \
       nose \
       mock \
       unittest2 \
       pySqsListener \
       weakrefset \
       rollbar \
       logdna \
       graphqlclient

# Enable playblasts with Quicktime
ENV LIBQUICKTIME_PLUGIN_DIR=/usr/autodesk/maya/lib

# Start Xvfb
# Provide an in-memory X-session for parts of Maya that require a GUI
# such as cmds.playblast()
ENV DISPLAY :99

# Run on user login, this has the limitation of being run
# each time a user logs into the Docker image. Suggestions
# are welcome to make this only run once at startup.
RUN echo "# Start Xvfb" >> ~/.bashrc && \
    echo "Xvfb :99 -screen 0 1024x768x16 2>/dev/null &" >> ~/.bashrc && \
    echo "while ! ps aux | \grep -q '[0]:00 Xvfb :99 -screen 0 1024x768x16';" >> ~/.bashrc && \
    echo "  do echo 'Waiting for Xvfb...'; sleep 1; done" >> ~/.bashrc

# Expose Python libraries to Maya
ENV PYTHONPATH=/usr/local/lib/python2.7/site-packages
RUN wget https://edutrial.autodesk.com/NET18SWDLD/2018/MAYA/ESD/Autodesk_Maya_2018_EN_Linux_64bit.tgz -O maya.tgz && \
    mkdir /maya && tar -xvf maya.tgz -C /maya && \
    rm maya.tgz && \
    rpm -Uvh /maya/Maya*.rpm && \
    rm -r /maya
RUN echo alias hpython="\"/usr/autodesk/maya/bin/mayapy\"" >> ~/.bashrc && \
    echo alias hpip="\"mayapy -m pip\"" >> ~/.bashrc
# Setup environment
ENV MAYA_LOCATION=/usr/autodesk/maya2018/
ENV PATH=$MAYA_LOCATION/bin:$PATH
# Workaround for "Segmentation fault (core dumped)"
# See https://forums.autodesk.com/t5/maya-general/render-crash-on-linux/m-p/5608552/highlight/true
ENV MAYA_DISABLE_CIP=1
ENV PYTHONHOME=$MAYA_LOCATION
ENV QT_PLUGIN_PATH=/usr/autodesk/maya2018/bin/../qt-plugins
ENV LD_LIBRARY_PATH=$MAYA_LOCATION/lib
#RUN mv /usr/local/lib/python2.7/site-packages/* /usr/autodesk/maya2018/lib/python2.7/site-packages
ENV PYTHONPATH=/usr/local/lib/python2.7/site-packages:/usr/autodesk/maya2018/lib/
# Cleanup
WORKDIR /root
