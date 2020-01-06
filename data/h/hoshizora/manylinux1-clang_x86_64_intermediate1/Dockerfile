FROM hoshizora/manylinux1-clang_x86_64:clang3

LABEL maintainer='amaya <mail@sapphire.in.net>'

WORKDIR /root

RUN set -eux && \
    `# Install deps` \
    yum install -y zlib-devel xz gcc && \
    `# Install clang 5.0.2` \
    cd && \
    curl http://releases.llvm.org/5.0.2/llvm-5.0.2.src.tar.xz \
      | xz -dc \
      | tar xp && \
    mv llvm-5.0.2.src llvm && \
    curl http://releases.llvm.org/5.0.2/cfe-5.0.2.src.tar.xz \
      | xz -dc \
      | tar xp && \
    mv cfe-5.0.2.src llvm/tools/clang && \
    curl http://releases.llvm.org/5.0.2/libcxx-5.0.2.src.tar.xz \
      | xz -dc \
      | tar xp && \
    mv libcxx-5.0.2.src llvm/projects/libcxx && \
    curl http://releases.llvm.org/5.0.2/libcxxabi-5.0.2.src.tar.xz \
      | xz -dc \
      | tar xp && \
    mv libcxxabi-5.0.2.src llvm/projects/libcxxabi && \
    curl http://releases.llvm.org/5.0.2/openmp-5.0.2.src.tar.xz \
      | xz -dc \
      | tar xp && \
    mv openmp-5.0.2.src llvm/projects/openmp && \
    mkdir llvm-build && \
    cd llvm-build && \
    cmake -G "Unix Makefiles" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_C_COMPILER=clang \
      -DCMAKE_CXX_COMPILER=clang++ \
      -DCMAKE_INSTALL_PREFIX=/usr/local \
      -DLLVM_ENABLE_LIBCXX=true \
      -DCLANG_DEFAULT_CXX_STDLIB=libc++ \
      -DPYTHON_EXECUTABLE=/opt/python/cp27-cp27m/bin/python \
      ../llvm

