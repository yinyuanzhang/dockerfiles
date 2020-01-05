FROM amd64/ubuntu:eoan

RUN apt-get update \
 && apt-get -y dist-upgrade \
 && apt-get -y install -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confnew -y --force-yes --no-install-suggests --no-install-recommends \
        debhelper default-jre-headless doxygen dpkg-dev \
        fakeroot git git2cl gnupg graphviz \
        libcppunit-dev libltdl-dev libpod-tree-perl \
        libtool locales lsb-release mscgen pandoc \
        pkg-config python3-software-properties \
        qt5-default qt5-qmake qtbase5-dev \
        qtbase5-dev-tools qttools5-dev \
        qttools5-dev-tools software-properties-common \
        wget binutils libiberty-dev liblog4cxx-dev \
        libboost-dev libz-dev \
 && apt-get autoremove -y --purge
