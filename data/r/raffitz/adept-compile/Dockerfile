#
#   Copyright 2018 Rafael Gonçalves
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

FROM gcc:7.3.0 AS build

ENV TARGET_PLATFORM riscv64-unknown-elf

# Package Dependencies
RUN apt-get update && apt-get install -y \
	libgmp-dev \
	libmpfr-dev \
	libmpc-dev \
	&& rm -rf /var/lib/apt/lists/*

# /usr/include/gmpxx.h
# /usr/include/x86_64-linux-gnu/gmp.h
# /usr/lib/x86_64-linux-gnu/libgmp.a
# /usr/lib/x86_64-linux-gnu/libgmp.so
# /usr/lib/x86_64-linux-gnu/libgmpxx.a
# /usr/lib/x86_64-linux-gnu/libgmpxx.so

# /usr/lib/x86_64-linux-gnu/libgmp.so.10
# /usr/lib/x86_64-linux-gnu/libgmp.so.10.3.2

# /usr/lib/x86_64-linux-gnu/libgmpxx.so.4
# /usr/lib/x86_64-linux-gnu/libgmpxx.so.4.5.2

# /usr/include/mpf2mpfr.h
# /usr/include/mpfr.h
# /usr/lib/x86_64-linux-gnu/libmpfr.a
# /usr/lib/x86_64-linux-gnu/libmpfr.so

# /usr/lib/x86_64-linux-gnu/libmpfr.so.4
# /usr/lib/x86_64-linux-gnu/libmpfr.so.4.1.5

# /usr/include/mpc.h
# /usr/lib/x86_64-linux-gnu/libmpc.a
# /usr/lib/x86_64-linux-gnu/libmpc.so

# /usr/lib/x86_64-linux-gnu/libmpc.so.3
# /usr/lib/x86_64-linux-gnu/libmpc.so.3.0.0

# Install riscv64-unknown-elf binutils

ENV BINUTILS_VERSION 2.29.1

WORKDIR "/root"

RUN wget https://ftp.gnu.org/gnu/binutils/binutils-${BINUTILS_VERSION}.tar.xz
RUN tar -xf binutils-${BINUTILS_VERSION}.tar.xz

WORKDIR "/root/binutils-${BINUTILS_VERSION}"

RUN ./configure --target=${TARGET_PLATFORM} --prefix=/usr --with-sysroot=/usr/${TARGET_PLATFORM} --with-gnu-as --with-gnu-ld --with-system-zlib --disable-nls --enable-multilib --enable-ld=default --enable-gold --enable-plugins --enable-deterministic-archives
RUN make
RUN make install

# The following files are necessary:
# /usr/bin/riscv64-unknown-elf-ld
# /usr/bin/riscv64-unknown-elf-objdump
# /usr/bin/riscv64-unknown-elf-size
# /usr/bin/riscv64-unknown-elf-addr2line
# /usr/bin/riscv64-unknown-elf-nm
# /usr/bin/riscv64-unknown-elf-strip
# /usr/bin/riscv64-unknown-elf-ld.bfd
# /usr/bin/riscv64-unknown-elf-strings
# /usr/bin/riscv64-unknown-elf-ar
# /usr/bin/riscv64-unknown-elf-objcopy
# /usr/bin/riscv64-unknown-elf-c++filt
# /usr/bin/riscv64-unknown-elf-as
# /usr/bin/riscv64-unknown-elf-gprof
# /usr/bin/riscv64-unknown-elf-elfedit
# /usr/bin/riscv64-unknown-elf-readelf
# /usr/bin/riscv64-unknown-elf-ranlib
# /usr/riscv64-unknown-elf/


# Install riscv64-unknown-elf gcc

ENV GCC_VERSION 7.3.0
ENV ISL_VERSION 0.18
ENV NEWLIB_VERSION 3.0.0

WORKDIR "/root"

RUN wget https://gcc.gnu.org/pub/gcc/releases/gcc-${GCC_VERSION}/gcc-${GCC_VERSION}.tar.xz
RUN wget http://isl.gforge.inria.fr/isl-${ISL_VERSION}.tar.bz2
RUN wget https://sourceware.org/pub/newlib/newlib-${NEWLIB_VERSION}.tar.gz
RUN wget https://aur.archlinux.org/cgit/aur.git/plain/newlib.patch?h=riscv64-unknown-elf-gcc -O newlib.patch
RUN tar -xf gcc-${GCC_VERSION}.tar.xz
RUN tar -xf isl-${ISL_VERSION}.tar.bz2
RUN tar -xf newlib-${NEWLIB_VERSION}.tar.gz

WORKDIR "/root/newlib-${NEWLIB_VERSION}"

RUN patch -Np1 -i ../newlib.patch

WORKDIR "/root/gcc-${GCC_VERSION}"

RUN ln -s ../isl-${ISL_VERSION} isl
RUN ln -s ../newlib-${NEWLIB_VERSION}/newlib
RUN ln -s ../newlib-${NEWLIB_VERSION}/libgloss
RUN echo ${GCC_VERSION} > gcc/BASE-VER

# hack! - some configure tests for header files using "$CPP $CPPFLAGS"
RUN sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" libiberty/configure gcc/configure

RUN mkdir -p "/root/build"

WORKDIR  "/root/build"

ENV CFLAGS_FOR_TARGET "-g -Os -ffunction-sections -fdata-sections"
ENV CXXFLAGS_FOR_TARGET "-g -Os -ffunction-sections -fdata-sections"

RUN /root/gcc-${GCC_VERSION}/configure \
	--target=${TARGET_PLATFORM} \
	--prefix=/usr \
	--with-sysroot=/usr/${TARGET_PLATFORM} \
	--with-native-system-header-lib=/include \
	--libexecdir=/usr/lib \
	--enable-languages=c,c++ \
	--enable-plugins \
	--disable-decimal-float \
	--disable-libffi \
	--disable-libgomp \
	--disable-libmudflap \
	--disable-libquadmath \
	--disable-libssp \
	--disable-libstdcxx-pch \
	--disable-nls \
	--disable-shared \
	--disable-threads \
	--disable-tls \
	--with-gnu-as \
	--with-gnu-ls \
	--with-system-zlib \
	--with-newlib \
	--with-headers=/usr/${TARGET_PLATFORM}/include \
	--with-python-dir=share/gcc-${TARGET_PLATFORM} \
	--with-gmp \
	--with-mpfr \
	--with-mpc \
	--with-isl \
	--with-libelf \
	--enable-gnu-indirect-function \
	--with-host-libstdcxx='-static-libgcc -Wl,-Bstatic,-lstdc++,-Bdynamic -lm' \
	--with-pkgversion='Adept Build Container' \
	--with-bugurl='https://github.com/raffitz/adept-compiler' \
	--disable-newlib-supplied-syscalls \
	--enable-newlib-reent-small \
	--disable-newlib-fvwrite-in-streamio \
	--disable-newlib-fseek-optimization \
	--disable-newlib-wide-orient \
	--enable-newlib-nano-malloc \
	--disable-newlib-unbuf-stream-opt \
	--enable-lite-exit \
	--enable-newlib-global-atexit \
	--enable-newlib-nano-formatted-io

RUN make INHIBIT_LIBC_CFLAGS='-DUSE_TM_CLONE_REGISTRY=0'

RUN mkdir -p /interim

RUN make -j1 DESTDIR="/interim" install

RUN find "/interim/usr/lib/gcc/${TARGET_PLATFORM}/${GCC_VERSION}" "/interim/usr/${TARGET_PLATFORM}/lib" -type f -and \( -name \*.a -or -name \*.o \) -exec ${TARGET_PLATFORM}-objcopy -R .comment -R .note -R .debug_info -R .debug_aranges -R .debug_pubnames -R .debug_pubtypes -R .debug_abbrev -R .debug_line -R .debug_str -R .debug_ranges -R .debug_loc '{}' \;

RUN find "/interim/usr/bin/" "/interim/usr/lib/gcc/${TARGET_PLATFORM}/${GCC_VERSION}" -type f -and \( -executable \) -exec strip '{}' \;

# RUN rm /interim/usr/lib/libcc1.*

RUN cp -r /interim/* /
RUN rm -rf /interim

# /usr/lib/gcc/riscv64-unknown-elf
# /usr/bin/riscv64-unknown-elf-c++
# /usr/bin/riscv64-unknown-elf-cpp
# /usr/bin/riscv64-unknown-elf-g++
# /usr/bin/riscv64-unknown-elf-gcc
# /usr/bin/riscv64-unknown-elf-gcc-7.3.0
# /usr/bin/riscv64-unknown-elf-gcc-ar
# /usr/bin/riscv64-unknown-elf-gcc-nm
# /usr/bin/riscv64-unknown-elf-gcc-ranlib
# /usr/bin/riscv64-unknown-elf-gcov
# /usr/bin/riscv64-unknown-elf-gcov-dump
# /usr/bin/riscv64-unknown-elf-gcov-tool

FROM debian:stretch-slim

ENV RISCV /usr

RUN apt-get update && apt-get install -y \
	libgmp10 \
	libgmpxx4ldbl \
	libmpfr4 \
	libmpc3 \
	make \
	&& rm -rf /var/lib/apt/lists/* \
	&& mkdir -p \
	/lib/x86_64-linux-gnu \
	/usr/riscv64-unknown-elf \
	/usr/lib/gcc/riscv64-unknown-elf
	
COPY --from=build /usr/bin/riscv64-unknown-elf-* /usr/bin/
COPY --from=build /usr/lib/gcc/riscv64-unknown-elf /usr/lib/gcc/riscv64-unknown-elf/
COPY --from=build /usr/riscv64-unknown-elf /usr/riscv64-unknown-elf/

RUN echo "Symlinking..." \
	&& ln -s /usr/bin/riscv64-unknown-elf-ld /usr/bin/riscv32-unknown-elf-ld \
	&& ln -s /usr/bin/riscv64-unknown-elf-objdump /usr/bin/riscv32-unknown-elf-objdump \
	&& ln -s /usr/bin/riscv64-unknown-elf-size /usr/bin/riscv32-unknown-elf-size \
	&& ln -s /usr/bin/riscv64-unknown-elf-addr2line /usr/bin/riscv32-unknown-elf-addr2line \
	&& ln -s /usr/bin/riscv64-unknown-elf-nm /usr/bin/riscv32-unknown-elf-nm \
	&& ln -s /usr/bin/riscv64-unknown-elf-strip /usr/bin/riscv32-unknown-elf-strip \
	&& ln -s /usr/bin/riscv64-unknown-elf-ld.bfd /usr/bin/riscv32-unknown-elf-ld.bfd \
	&& ln -s /usr/bin/riscv64-unknown-elf-strings /usr/bin/riscv32-unknown-elf-strings \
	&& ln -s /usr/bin/riscv64-unknown-elf-ar /usr/bin/riscv32-unknown-elf-ar \
	&& ln -s /usr/bin/riscv64-unknown-elf-objcopy /usr/bin/riscv32-unknown-elf-objcopy \
	&& ln -s /usr/bin/riscv64-unknown-elf-c++filt /usr/bin/riscv32-unknown-elf-c++filt \
	&& ln -s /usr/bin/riscv64-unknown-elf-as /usr/bin/riscv32-unknown-elf-as \
	&& ln -s /usr/bin/riscv64-unknown-elf-gprof /usr/bin/riscv32-unknown-elf-gprof \
	&& ln -s /usr/bin/riscv64-unknown-elf-elfedit /usr/bin/riscv32-unknown-elf-elfedit \
	&& ln -s /usr/bin/riscv64-unknown-elf-readelf /usr/bin/riscv32-unknown-elf-readelf \
	&& ln -s /usr/bin/riscv64-unknown-elf-ranlib /usr/bin/riscv32-unknown-elf-ranlib \
	&& ln -s /usr/bin/riscv64-unknown-elf-c++ /usr/bin/riscv32-unknown-elf-c++ \
	&& ln -s /usr/bin/riscv64-unknown-elf-cpp /usr/bin/riscv32-unknown-elf-cpp \
	&& ln -s /usr/bin/riscv64-unknown-elf-g++ /usr/bin/riscv32-unknown-elf-g++ \
	&& ln -s /usr/bin/riscv64-unknown-elf-gcc /usr/bin/riscv32-unknown-elf-gcc \
	&& ln -s /usr/bin/riscv64-unknown-elf-gcc-7.3.0 /usr/bin/riscv32-unknown-elf-gcc-7.3.0 \
	&& ln -s /usr/bin/riscv64-unknown-elf-gcc-ar /usr/bin/riscv32-unknown-elf-gcc-ar \
	&& ln -s /usr/bin/riscv64-unknown-elf-gcc-nm /usr/bin/riscv32-unknown-elf-gcc-nm \
	&& ln -s /usr/bin/riscv64-unknown-elf-gcc-ranlib /usr/bin/riscv32-unknown-elf-gcc-ranlib \
	&& ln -s /usr/bin/riscv64-unknown-elf-gcov /usr/bin/riscv32-unknown-elf-gcov \
	&& ln -s /usr/bin/riscv64-unknown-elf-gcov-dump /usr/bin/riscv32-unknown-elf-gcov-dump \
	&& ln -s /usr/bin/riscv64-unknown-elf-gcov-tool /usr/bin/riscv32-unknown-elf-gcov-tool
