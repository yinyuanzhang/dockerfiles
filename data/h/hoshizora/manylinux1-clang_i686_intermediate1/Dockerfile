FROM quay.io/pypa/manylinux1_i686

LABEL maintainer='amaya <mail@sapphire.in.net>'

WORKDIR /root

RUN set -eux && \
    `# Install deps` \
    yum install -y zlib-devel xz && \
    `# Install cmake 3.11.4` \
    wget --no-check-certificate https://cmake.org/files/v3.11/cmake-3.11.4.tar.gz -O - \
      | tar xz && \
    cd cmake-3.11.4 && \
    ./configure --system-curl && \
    make -j2 && \
    make install && \
    mv install_manifest.txt /usr/local/share/cmake-3.11 && \
    `# Install clang 3.9.1` \
    cd && \
    wget http://releases.llvm.org/3.9.1/llvm-3.9.1.src.tar.xz -O - \
      | xz -dc \
      | tar xp && \
    mv llvm-3.9.1.src llvm && \
    wget http://releases.llvm.org/3.9.1/cfe-3.9.1.src.tar.xz -O - \
      | xz -dc \
      | tar xp && \
    mv cfe-3.9.1.src llvm/tools/clang && \
    wget http://releases.llvm.org/3.9.1/libcxx-3.9.1.src.tar.xz -O - \
      | xz -dc \
      | tar xp && \
    mv libcxx-3.9.1.src llvm/projects/libcxx && \
    wget http://releases.llvm.org/3.9.1/libcxxabi-3.9.1.src.tar.xz -O - \
      | xz -dc \
      | tar xp && \
    mv libcxxabi-3.9.1.src llvm/projects/libcxxabi && \
    wget http://releases.llvm.org/3.9.1/openmp-3.9.1.src.tar.xz -O - \
      | xz -dc \
      | tar xp && \
    mv openmp-3.9.1.src llvm/projects/openmp && \
    mkdir llvm-build && \
    cd llvm-build && \
    cmake -G "Unix Makefiles" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=/usr/local \
      -DPYTHON_EXECUTABLE=/opt/python/cp27-cp27m/bin/python \
      ../llvm

