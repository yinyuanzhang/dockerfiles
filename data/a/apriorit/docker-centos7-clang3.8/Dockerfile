FROM centos:7
MAINTAINER kotik <obrbkru@apriorit.com>

#build install clang 3.8.0
RUN yum -y install epel-release python-requests subversion && \
pushd /etc/yum.repos.d/ && curl https://copr.fedorainfracloud.org/coprs/alonid/llvm-3.8.0/repo/epel-7/alonid-llvm-3.8.0-epel-7.repo -O && popd && \
yum install -y clang-3.8.0 clang-3.8.0-devel.x86_64 llvm-3.8.0-devel

#building and installing of clang c++ library for better c++11 support
# http://stackoverflow.com/questions/25840088/how-to-build-libcxx-and-libcxxabi-by-clang-on-centos-7/25840107#25840107
# use "one command" style because of Docker copypaste convenience
#*******************************************
RUN yum install -y cmake3 cmake make wget

RUN export PATH=$PATH:/opt/llvm-3.8.0/bin/ && \
export CXX=/opt/llvm-3.8.0/bin/clang++ && \
export CC=/opt/llvm-3.8.0/bin/clang && \
libcxx="libcxx-3.8.1.src" && \
tmp="/tmp/buildTemp" && \
mkdir $tmp && \
cd $tmp && \
wget "http://llvm.org/releases/3.8.1/$libcxx.tar.xz" && \
tar xf "$libcxx.tar.xz" && \
mkdir $tmp/$libcxx/build && cd $tmp/$libcxx/build && \
cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr $tmp/$libcxx && \
make install && \
ln -s /usr/lib/libc++.so.1 /lib64 && \
libcxxabi="libcxxabi-3.8.1.src" && \
cd $tmp && wget "http://llvm.org/releases/3.8.1/$libcxxabi.tar.xz" && \
tar xf "$libcxxabi.tar.xz" && \
mkdir $tmp/$libcxxabi/build && cd $tmp/$libcxxabi/build && \
cd $tmp/$libcxxabi && \
cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_CXX_FLAGS="-std=c++11" -DLIBCXXABI_LIBCXX_INCLUDES=/usr/include/c++/v1/ && \
make install && \
ln -s /usr/lib/libc++abi.so.1 /lib64 && \
cd $tmp/$libcxxabi/build && \
cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DLIBCXX_CXX_ABI=libcxxabi -DLIBCXX_CXX_ABI_INCLUDE_PATHS=$tmp/$libcxxabi/include $tmp/$libcxx && \
make install && \
cd /tmp && \
rm -rf $tmp
#*******************************************
