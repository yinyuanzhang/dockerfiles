###############################################################################
# simage:fedora
###############################################################################
# /
# |-- export []   <-- output package directory volume
# |-- import [ro]	<-- input source repository volume
# 
# Build:
# docker build -t ggabbiani/simage:fedora .
# docker build --build-arg version=30 -t ggabbiani/simage:fedora .
# 
# Run:
# docker run -it -v <sources>:/import:ro -v <artefacts>:/export ggabbiani/simage:fedora
# docker run -it ggabbiani/simage:fedora bash
###############################################################################
ARG version=29
FROM fedora:$version
LABEL maintainer="giampiero@gabbiani.org"

###############################################################################
# system setup
RUN  dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
  && dnf update -y
RUN dnf install -y \
  rpm-build \
  vim \
  make \
  cmake \ 
  doxygen \ 
  graphviz \
  gcc-c++ \
  rpmlint \
  git \
  sudo

###############################################################################
# simage pre requisites install
RUN dnf install -y \
  giflib-devel \
  libjpeg-turbo-devel \
  zlib-devel \
  libpng-devel \
  libtiff-devel \
  libvorbis-devel \
  libsndfile-devel \
  xvidcore-devel \
  libquicktime-devel \
  qt5-qtbase-devel \
  qt5-doctools

###############################################################################
# copy entry point
COPY entry-point.sh /usr/bin/entry-point
RUN chmod +x /usr/bin/entry-point

###############################################################################
# defaults for building from a mounted project source
CMD /usr/bin/entry-point -- -DCMAKE_BUILD_TYPE=RelWithDebInfo -DOPTION_PKG_DEBUGINFO=ON -DSIMAGE_BUILD_DOCUMENTATION=OFF
###############################################################################
# entrypoint
#ENTRYPOINT [ "/usr/bin/entry-point" ]
# defaults parameters for ENTRYPOINT
#CMD  [ \
#  "--" \
#  ,"-DCMAKE_BUILD_TYPE=RelWithDebInfo" \
#  ,"-DOPTION_PKG_DEBUGINFO=ON" \
#  ,"-DSIMAGE_BUILD_DOCUMENTATION=OFF" \
#]