FROM centos:centos7.4.1708


###############################################################################
# General update
###############################################################################
RUN yum update -y


###############################################################################
# Repositories
###############################################################################
# EPEL
RUN yum --enablerepo=extras install epel-release -y

# Python3
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm

# FFMPEG
RUN rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
RUN yum -y install http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm


###############################################################################
# System dependencies
###############################################################################
RUN yum update -y
RUN yum groupinstall "Development tools" -y
RUN yum install -y --skip-broken \
    autoconf-2.69 \
    automake-1.13.4 \
    atlas-devel-3.10.1 \
    bc-1.06.95 \
    binutils-2.27 \
    blas-devel-3.4.2 \
    boost-1.53.0 \
    boost-devel-1.53.0 \
    build-essential \
    cmake-2.8.12.2 \
    cmake3-3.11.2 \
    expect-5.45 \
    epel-release-7 \
    ffmpeg-2.6.8 \
    ffmpeg-devel-2.6.8 \
    flex-2.5.37 \
    freeglut-devel-2.8.1 \
    freetype-2.4.11 \
    freetype-devel-2.4.11 \
    future \
    gcc-c++-4.8.5 \
    gcc-4.8.5 \
    gettext-0.19.8.1 \
    git-1.8.3.1 \
    glibc-devel-2.17 \
    glibc-devel-2.17-222.el7.i686 \
    gtk2-devel-2.24.31 \
    gmp-devel-6.0.0 \
    hdf5-devel-1.8.12 \
    htop-2.1.0 \
    java-1.8.0-openjdk-devel \
    mpfr-devel-3.1.1 \
    libmpc-devel-1.0.1 \
    lapack-devel-3.4.2 \
    lcms2-devel-2.6 \
    libffi-devel-3.0.13 \
    libgcc-4.8.5-28.el7_5.1.i686 \
    libgfortran-4.8.5 \
    libjpeg-devel \
    libjpeg-turbo-devel-1.2.90 \
    libmpc-devel-1.0.1 \
    libpng-devel-1.5.13 \
    libraqm-devel-0.1.1 \
    libsndfile-1.0.25 \
    libSM-1.2.2 \
    libtiff-devel-4.0.3 \
    libtool-2.4.2 \
    libwebp-devel-0.3.0 \
    libXext-1.3.3 \
    libXi-devel-1.7.9 \
    libXmu-devel-1.1.2 \
    make-3.82 \
    mlocate-0.26 \
    mpfr-devel-3.1.1 \
    net-tools-2.0 \
    numactl-2.0.9 \
    numpy-1.7.1 \
    ntp-4.2.6p5 \
    openssh-clients-7.4p1 \
    openssh-server-7.4p1 \
    openssl-devel-1.0.2k \
    openssl-libs-1.0.2k \
    patch-2.7.1 \
    perf-3.10.0 \
    pkgconfig-0.27.1 \
    python-devel-2.7.5 \
    python-pip \
    python36u-3.6.5 \
    screen-4.1.0 \
    suitesparse-devel-4.0.2 \
    sysstat-10.1.5 \
    tbb-devel-4.1 \
    tcl-devel-8.5.13 \
    telnet-0.17 \
    texinfo-5.1 \
    tk-devel-8.5.13 \
    tkinter-2.7.5 \
    vim \
    wget-1.14 \
    which-2.20 \
    zlib-devel-1.2.7

###############################################################################
# Others
###############################################################################
RUN echo 'export JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk' >> ~/.bashrc; \
    echo 'export JRE_HOME=/usr/lib/jvm/jre' >> ~/.bashrc; \
    echo 'export PATH='"${PATH}":'$JAVA_HOME/bin' >> ~/.bashrc
RUN rm -f /usr/bin/python3 ;\
    cp /usr/bin/python3.6 /usr/bin/python3


###############################################################################
# Install Python3 dependencies
###############################################################################
RUN python3 -m ensurepip; \
    python3 -m pip install --upgrade pip==9.0.3; \
    python3 -m pip install PyYAML==3.12; \
    python3 -m pip install Flask==0.12.2; \
    python3 -m pip install Flask-CORS==3.0.3; \
    python3 -m pip install requests==2.18.4


###############################################################################
# Install Python2 dependencies
###############################################################################
RUN python2 -m pip install --upgrade pip==9.0.3; \
    python2 -m pip install requests==2.18.4; \
    python2 -m pip install setuptools==0.9.8; \
    python2 -m pip install enum34==1.1.6; \
    python2 -m pip install futures==3.2.0; \
    python2 -m pip install grpcio==1.12.0; \
    python2 -m pip install numpy==1.14.3; \
    python2 -m pip install h5py==2.7.1; \
    python2 -m pip install kafka==1.3.5; \
    python2 -m pip install mock==2.0.0; \
    python2 -m pip install pexpect==4.5.0; \
    python2 -m pip install protobuf==3.5.2.post1; \
    python2 -m pip install pyspark==2.3.1; \
    python2 -m pip install python-Levenshtein==0.12.0; \
    python2 -m pip install python-speech-features==0.6; \
    python2 -m pip install PySoundFile==0.9.0.post1; \
    python2 -m pip install psutil==5.4.5; \
    python2 -m pip install requests==2.18.4; \
    python2 -m pip install scipy==1.1.0; \
    python2 -m pip install scikit-learn==0.19.1; \
    python2 -m pip install six==1.11.0; \
    python2 -m pip install tqdm==4.23.3; \
    python2 -m pip install wheel; \
    python2 -m pip install matplotlib==2.2.2; \
    python2 -m pip install Pillow==5.1.0; \
    python2 -m pip install scikit-image==0.13.1; \
    python2 -m pip install opencv-python==3.4.0.14; \
    python2 -m pip install paramiko==2.4.1
