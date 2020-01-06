#
# 2018-2019 © BIM & Scan® Ltd.
# See 'README.md' in the project root for more information.
#
FROM conanio/clang7
MAINTAINER Neil Hyland <neil.hyland@bimandscan.com>

# Install and configure dependencies:
RUN sudo apt-get -qq update && \
    sudo apt-get -qq install -y --no-install-recommends valgrind \
                                                        autotools-dev \
                                                        autoconf \
                                                        automake \
                                                        doxygen \
                                                        gcovr \
                                                        curl \
                                                        lldb \
                                                        libomp-dev \
                                                        libopenmpi-dev

ENV GIT_LFS_VERSION=2.7.0
ENV CONAN_CPU_COUNT=2
ENV LDFLAGS=-Wl,--no-as-needed

# Install Git LFS:
RUN wget https://github.com/git-lfs/git-lfs/releases/download/v$GIT_LFS_VERSION/git-lfs-linux-amd64-v$GIT_LFS_VERSION.tar.gz -O git_lfs.tar.gz && \
    mkdir git_lfs && \
    tar -xzf git_lfs.tar.gz -C git_lfs && \
    rm git_lfs.tar.gz && \
    sudo chmod +x ./git_lfs/install.sh && \
    sudo bash -c ./git_lfs/install.sh

# Add remote(s):
RUN conan remote add "bincrafters" "https://api.bintray.com/conan/bincrafters/public-conan"
RUN mkdir -p "/home/conan/.conan/profiles"

# Install basic build profiles:
RUN echo "\n\
[settings]\n\
os=Linux\n\
os_build=Linux\n\
arch=x86_64\n\
arch_build=x86_64\n\
compiler=clang\n\
compiler.version=$LLVM_VERSION\n\
compiler.libcxx=libstdc++11\n\
build_type=Release\n\n\
[options]\n\
[build_requires]\n\
[env]\n\
" > "/home/conan/.conan/profiles/default"

RUN echo "\n\
[settings]\n\
os=Linux\n\
os_build=Linux\n\
arch=x86_64\n\
arch_build=x86_64\n\
compiler=clang\n\
compiler.version=$LLVM_VERSION\n\
compiler.libcxx=libstdc++11\n\
build_type=Release\n\n\
[options]\n\
[build_requires]\n\
[env]\n\
" > "/home/conan/.conan/profiles/Release"

RUN echo "\n\
[settings]\n\
os=Linux\n\
os_build=Linux\n\
arch=x86_64\n\
arch_build=x86_64\n\
compiler=clang\n\
compiler.version=$LLVM_VERSION\n\
compiler.libcxx=libstdc++11\n\
build_type=Debug\n\n\
[options]\n\
[build_requires]\n\
[env]\n\
" > "/home/conan/.conan/profiles/Debug"

RUN echo "\n\
[settings]\n\
os=Linux\n\
os_build=Linux\n\
arch=x86_64\n\
arch_build=x86_64\n\
compiler=clang\n\
compiler.version=$LLVM_VERSION\n\
compiler.libcxx=libstdc++11\n\
build_type=RelWithDebInfo\n\n\
[options]\n\
[build_requires]\n\
[env]\n\
" > "/home/conan/.conan/profiles/RelWithDebInfo"

# Prepare workspace area:
WORKDIR "/home/conan"
