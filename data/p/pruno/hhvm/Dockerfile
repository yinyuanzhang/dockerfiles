FROM centos:centos7

# Install Devtools
RUN yum install -y \
  wget \
  tar \
  make \
  libtool \
  git \
  gcc-c++

# Install GCC
WORKDIR /makes/gcc
RUN yum install -y \
    libgcc \
    glibc-devel \
    binutils \
    gzip \
    bzip2 \
    perl \
    zip \
    unzip \
  && wget ftp://ftp.gnu.org/gnu/gcc/gcc-4.9.2/gcc-4.9.2.tar.gz -O gcc.tar.gz \
  && tar -xzf gcc.tar.gz -C . --strip-components=1 \
  && wget -nv https://gmplib.org/download/gmp-6.0.0/gmp-6.0.0.tar.bz2 -O gmp.tar.bz2 \
  && mkdir gmp \
  && tar -xjf gmp.tar.bz2 -C gmp --strip-components=1 \
  && wget -nv http://www.mpfr.org/mpfr-current/mpfr-3.1.3.tar.gz -O mpfr.tar.gz \
  && mkdir mpfr \
  && tar -xzf mpfr.tar.gz -C mpfr --strip-components=1 \
  && wget -nv http://www.multiprecision.org/mpc/download/mpc-1.0.3.tar.gz -O mpc.tar.gz \
  && mkdir mpc \
  && tar -xzf mpc.tar.gz -C mpc --strip-components=1 \
  && wget ftp://ftp.irisa.fr/pub/mirrors/gcc.gnu.org/gcc/infrastructure/isl-0.12.2.tar.bz2 -O isl.tar.bz2 \
  && mkdir isl \
  && tar -xjf isl.tar.bz2 -C isl --strip-components=1 \
  && wget http://bastoul.net/cloog/pages/download/cloog-0.18.2.tar.gz -O cloog.tar.gz \
  && mkdir cloog \
  && tar -xzf cloog.tar.gz -C cloog --strip-components=1 \
  && ./configure --enable-languages=c,c++,fortran --disable-multilib \
  && make \
  && yum remove -y \
    gcc \
    gcc-c++ \
    cpp \
  && make install

