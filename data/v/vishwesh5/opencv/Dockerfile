FROM vishwesh5/opencv:base
LABEL maintainer="Vishwesh Ravi Shrimali <vishweshshrimali5@gmail.com>"

ARG NB_USER="opencv"

ARG NB_UID="1000"

ARG NB_GID="100"

# Configure environment
ENV SHELL=/bin/bash \
    NB_USER=$NB_USER \
    NB_UID=$NB_UID \
    NB_GID=$NB_GID \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

# Setup Environment Variable
ENV cvVersion="3.4.5"
ENV cwd="/opt"
ENV HOME=/home/$NB_USER

USER root

WORKDIR $cwd

RUN git clone https://github.com/opencv/opencv.git && \
	cd opencv && \
	git checkout tags/"$cvVersion" && \
	cd ..

RUN git clone https://github.com/opencv/opencv_contrib.git && \
	cd opencv_contrib && \
	git checkout tags/"$cvVersion" && \
	cd ..

RUN cd opencv && \
	mkdir build && \
	cd build && \
	cmake -DCMAKE_BUILD_TYPE=RELEASE \
	-DCMAKE_INSTALL_PREFIX=/usr/local \
	-DINSTALL_C_EXAMPLES=ON \
	-DWITH_TBB=ON \
	-DWITH_V4L=ON \
	-DWITH_QT=ON \
	-DWITH_OPENGL=ON \
	-DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
        -DOPENCV_SKIP_PYTHON_MODULE=ON .. && \
	make -j4 && make install && \
	cd ..

RUN /bin/sh -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf'

RUN ldconfig

WORKDIR $cwd

RUN rm -rf $cwd/opencv && \
    rm -rf $cwd/opencv_contrib

USER $NB_UID

WORKDIR $HOME
