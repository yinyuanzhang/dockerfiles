FROM ubuntu:18.04
LABEL maintainer="Kyungmin Lee <kyungmin.lee.42@gmail.com>"

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y build-essential curl gfortran gnuplot ifeffit dbus-x11 libx11-dev libncurses5-dev libpng-dev libgif-dev libwxgtk3.0-dev
RUN apt-get install -y \
    libifeffit-perl \
    libwx-perl \
    libmodule-install-perl \
    libmodule-build-perl \
    libarchive-zip-perl \
    libcapture-tiny-perl \
    libchemistry-elements-perl \
    libconfig-ini-perl \
    libconst-fast-perl \
    libdatetime-perl \
    libencoding-fixlatin-perl \
    libencoding-fixlatin-xs-perl \
    libfile-copy-recursive-perl \
    libfile-countlines-perl \
    libfile-monitor-lite-perl \
    libfile-which-perl \
    libgraph-perl \
    libgraphics-gnuplotif-perl \
    libheap-perl \
    libhtml-parser-perl \
    libjson-perl \
    libmath-combinatorics-perl \
    libmath-derivative-perl \
    libmath-random-perl \
    libmath-round-perl \
    libmath-spline-perl \
    libmoose-perl \
    libmoosex-aliases-perl \
    libmoosex-types-perl \
    libmoosex-types-laxnum-perl \
    libpdl-stats-perl \
    libpod-pom-perl \
    libregexp-assemble-perl \
    libregexp-common-perl \
    libsoap-lite-perl \
    libspreadsheet-writeexcel-perl \
    libstatistics-descriptive-perl \
    libstring-random-perl \
    libterm-sk-perl \
    libterm-twiddle-perl \
    libtext-template-perl \
    libtext-unidecode-perl \
    libtree-simple-perl \
    libwant-perl \
    libwx-perl \
    libxmlrpc-lite-perl \
    libyaml-tiny-perl \
    librpc-xml-perl \
    libfile-slurper-perl \
    libpod-projectdocs-perl
RUN apt-get install -y xterm

RUN mkdir -p /home/user
WORKDIR /home/user
RUN curl https://codeload.github.com/bruceravel/demeter/tar.gz/0.9.26 | tar xzv
WORKDIR /home/user/demeter-0.9.26

RUN perl -I. ./Build.PL
RUN ./Build
RUN ./Build install

WORKDIR /
