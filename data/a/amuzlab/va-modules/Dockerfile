# STEP BASE IMAGE
    FROM amuzlab/va-modules:centos7.4-cuda10.1-devel-base
    LABEL maintainer "AMUZLAB CORPORATION <amuzlab@amuzlab.com>"

# STEP nv-codec-headers for using nvidia-graphic card on ffmpeg
    RUN git clone https://github.com/FFmpeg/nv-codec-headers /root/nv-codec-headers && \
      cd /root/nv-codec-headers && \
      make -j8 && \
      make install -j8

# STEP Build FFmpeg
    # install Prerequisite
    RUN yum install -y autoconf automake bzip2 bzip2-devel freetype-devel mercurial pkgconfig gtk3 gtk3-devel libv4l libv4l-devel && \
	mkdir /root/ffmpeg

    # Build Nasm
    RUN cd /root/ffmpeg && curl -O -L https://www.nasm.us/pub/nasm/releasebuilds/2.14.02/nasm-2.14.02.tar.bz2 && \
	tar xjvf nasm-2.14.02.tar.bz2 && \
	cd nasm-2.14.02 && \
	./autogen.sh && \
	./configure --prefix="/usr/local" --bindir="/usr/local/bin" && \
	make -j12 && make install

    # Build Yasm
    RUN cd /root/ffmpeg && curl -O -L https://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz && \
	tar xzvf yasm-1.3.0.tar.gz && \
	cd yasm-1.3.0 && \
	./configure --prefix="/usr/local" --bindir="/usr/local/bin" && \
	make -j12 && make install

    # Build x264
    RUN cd /root/ffmpeg && git clone --depth 1 https://code.videolan.org/videolan/x264.git --branch=stable && \
    cd x264 && \
    PKG_CONFIG_PATH="/usr/local/lib/pkgconfig" ./configure --prefix="/usr/local" --bindir="/usr/local/bin" --enable-static --enable-shared&& \
    make -j12 && make install

    # Build x265
    RUN cd /root/ffmpeg && hg clone https://bitbucket.org/multicoreware/x265 && \
	cd x265/build/linux && \
	cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="/usr/local" -DENABLE_SHARED:bool=on ../../source && \
	make -j12 && make install

    # Build fdk_aac
    RUN cd /root/ffmpeg && git clone --depth 1 https://github.com/mstorsjo/fdk-aac && \
	cd fdk-aac && \
	autoreconf -fiv && \
	./configure --prefix="/usr/local" --enable-shared && \
	make -j12 && make install

    # Build libmp3lame
    RUN cd /root/ffmpeg && curl -O -L https://downloads.sourceforge.net/project/lame/lame/3.100/lame-3.100.tar.gz && \
	tar xzvf lame-3.100.tar.gz && \
	cd lame-3.100 && \
	./configure --prefix="/usr/local" --bindir="/usr/local/bin" --enable-shared --enable-nasm && \
	make -j12 && make install

    # Build libopus
    RUN cd /root/ffmpeg && curl -O -L https://archive.mozilla.org/pub/opus/opus-1.3.1.tar.gz && \
	tar xzvf opus-1.3.1.tar.gz && \
	cd opus-1.3.1 && \
	./configure --prefix="/usr/local" --enable-shared && \
	make -j12 && make install

    # Build libvpx
    RUN cd /root/ffmpeg && git clone --depth 1 https://chromium.googlesource.com/webm/libvpx.git && \
	cd libvpx && \
	./configure --prefix="/usr/local" --enable-shared --disable-examples --disable-unit-tests --enable-vp9-highbitdepth --as=yasm && \
	make -j12 && make install

    # Build FFMpeg with CUDA
    RUN cd /root/ffmpeg && curl -O -L https://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2 && \
	tar xjvf ffmpeg-snapshot.tar.bz2 && \
	cd ffmpeg && \
	PATH="/usr/local/bin:$PATH" PKG_CONFIG_PATH="/usr/local/lib/pkgconfig" ./configure \
	--prefix="/usr/local" \
	--pkg-config-flags="--static" \
	--extra-cflags="-I/usr/local/include" \
	--extra-ldflags="-L/usr/local/lib" \
	--extra-libs=-lpthread \
	--extra-libs=-lm \
	--bindir="/usr/local/bin" \
	--enable-gpl \
	--enable-libfdk_aac \
	--enable-libfreetype \
	--enable-libmp3lame \
	--enable-libopus \
	--enable-libvpx \
	--enable-gpl \
	--enable-libx264 \
	--enable-libx265 \
	--enable-nonfree \
	--enable-cuda-nvcc \
	--enable-libnpp \
	--enable-nvenc \
	--enable-nvdec \
	--enable-cuvid \
	--extra-cflags="-I/usr/local/cuda/include" \
	--extra-ldflags="-L/usr/local/cuda/lib64" \
	--enable-shared \
	--enable-pic && \
        make -j12 && make install

    RUN echo "/usr/local/lib" >> /etc/ld.so.conf.d/ffmpeg.conf
    RUN ldconfig

WORKDIR /home
