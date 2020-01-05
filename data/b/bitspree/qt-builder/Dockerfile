FROM ubuntu:18.04

LABEL authors="garaone@co3.de"

ENV QT=5.12.6
ENV QTM=5.12
ENV FIREBASE_CPP=6.8.0

ENV DEBIAN_FRONTEND noninteractive
ENV QT_PATH /opt/qt
ENV QT_BASE_DIR=$QT_PATH

ENV QT_ARCH ${QT_PATH}/${QT}/gcc_64
# ENV QT_QPA_PLATFORM=minimal
ENV LD_LIBRARY_PATH=$QT_PATH/lib/x86_64-linux-gnu:$QT_PATH/lib:$LD_LIBRARY_PATH
ENV PKG_CONFIG_PATH=$QT_BAQT_PATHSE_DIR/lib/pkgconfig:$PKG_CONFIG_PATH
ENV PATH=${PATH}:${QT_ARCH}/bin


# download QT
ADD qt-installer-noninteractive.qs /tmp/qt/script.qs
# ADD ./qt-opensource-linux-x64-${QT}.run /tmp/qt/installer.run
ADD http://download.qt.io/official_releases/qt/${QTM}/${QT}/qt-opensource-linux-x64-${QT}.run /tmp/qt/installer.run

# download FIREBASE_CPP
# ADD ./firebase_cpp_sdk_${FIREBASE_CPP}.zip /install/
ADD https://dl.google.com/firebase/sdk/cpp/firebase_cpp_sdk_${FIREBASE_CPP}.zip /install/

# install
RUN rm /bin/sh && ln -s /bin/bash /bin/sh \
    \
    && apt-get update -q \
    && apt-get install -q -y --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
        git \
        libfontconfig1 \
        libglib2.0-dev \
        libglu1-mesa-dev \
        libice6 \
        libpulse-dev \
        libsm6 \
        libxext6 \
        libxrender1 \
        locales \
        mesa-common-dev \
        openssh-client \
        p7zip-full \
        xvfb \
        unzip \
        wget \
    \
    && chmod +x /tmp/qt/installer.run \
    && xvfb-run /tmp/qt/installer.run -v --script /tmp/qt/script.qs \
     | egrep -v '\[[0-9]+\] Warning: (Unsupported screen format)|((QPainter|QWidget))' \
    && rm -rf /tmp/qt \
    \
    && locale-gen en_US.UTF-8 \
    && dpkg-reconfigure locales \
    \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf \
        /tmp/* \
        /var/tmp/* \
        /var/lib/cache/* \
        /var/lib/log/*
        # /var/lib/apt/lists/* 
        # /var/lib/dpkg/*

CMD ["/bin/bash"]
