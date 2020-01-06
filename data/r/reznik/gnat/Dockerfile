FROM ubuntu:19.04
ENV PATH=/gnat-llvm/llvm-interface/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
RUN apt-get update && apt-get install -y \
 cmake \
 gprbuild \
 g++ \
 gnat \
 git \
 wget \
 gnupg \
 subversion \
 && echo "deb http://apt.llvm.org/disco/ llvm-toolchain-disco-9 main" \
   > /etc/apt/sources.list.d/llvm.list \
 && wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && apt-get update \
 && apt-get install -y llvm-9-dev clang-9 lldb-9 lld-9 \
 && git clone https://github.com/AdaCore/gnat-llvm.git /gnat-llvm/ \
 && svn co svn://gcc.gnu.org/svn/gcc/trunk/gcc/ada \
    /gnat-llvm/llvm-interface/gnat_src \
 && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-9 100 \
     --slave /usr/bin/llvm-config llvm-config /usr/bin/llvm-config-9 \
 && make -C /gnat-llvm \
 && apt-get purge -y --auto-remove gnat git wget gnupg subversion \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
