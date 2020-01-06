FROM centos:latest
WORKDIR /root
RUN yum -y install gcc lbzip2 bzip2 make file patch openssl-devel net-tools tcpdump iproute
RUN curl -o curl-loader-0.56.tar.bz2  https://netix.dl.sourceforge.net/project/curl-loader/curl-loader-stable/curl-loader-0.56/curl-loader-0.56.tar.bz2 && tar -xf curl-loader-0.56.tar.bz2
WORKDIR curl-loader-0.56/
RUN make cleanall && make optimize=1 debug=0 && make install
WORKDIR /root
# Cleanup
RUN rm -rf curl-loader-*
