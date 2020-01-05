FROM archlinux/base

RUN pacman -Syu --needed --noconfirm make clang-tools-extra python git wxgtk2 glu pkg-config boost-libs boost openmp tup valgrind gcc-fortran autogen glew ragel && pacman -Scc --noconfirm

ENV CC clang
ENV CXX clang++

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
RUN locale-gen
ENV LANG en_US.UTF-8
