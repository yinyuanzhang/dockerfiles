FROM ubuntu:trusty

RUN apt-get update \
&& apt-get install -y git 
RUN git clone https://github.com/facebook/fbctf \
&& cd fbctf \
&& apt-get install -y binutils fontconfig-config fonts-dejavu-core imagemagick-common
  libboost-context1.54.0 libboost-filesystem1.54.0
  libboost-program-options1.54.0 libboost-regex1.54.0 libboost-system1.54.0
  libboost-thread1.54.0 libc-client2007e libdouble-conversion1 libelf1
  libevent-2.0-5 libfftw3-double3 libfontconfig1 libfreetype6 libgd3
  libgflags2 libgmp10 libgomp1 libgoogle-glog0 libicu52 libjasper1 libjbig0
  libjemalloc1 libjpeg-turbo8 libjpeg8 liblcms2-2 liblqr-1-0 libltdl7 liblz4-1
  libmagickcore5 libmagickwand5 libmcrypt4 libmemcached10 libmysqlclient18
  libnuma1 libonig2 libpq5 libsnappy1 libtbb2 libtiff5 libunwind8 libvpx1
  libxml2 libxpm4 libxslt1.1 libyaml-0-2 lsof mlock mysql-common \
&& ./extra/provision.sh -m prod -s .

CMD ["/bin/bash"]
