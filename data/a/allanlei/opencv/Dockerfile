FROM    alpine:edge

ENV     VERSION 3.1.0

COPY    src/opencv /opt/src/opencv
RUN     echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
        apk --no-cache add --virtual .builddeps \
            build-base \
            cmake \
            linux-headers \
            python-dev \
            py-numpy-dev
            # openjdk8 \

            # libtbb \
            # libtbb-dev \
            # libjpeg  \
            # libjpeg-turbo-dev \
            # libpng-dev \
            # libjasper \
            # tiff-dev \
            # libwebp-dev
            # ffmpeg-dev
            # py-scipy-dev \
            # gsl \
            # libavc1394-dev \
            # libdc1394-dev \
RUN     cd /opt/src/opencv && \
        cmake \
            -D CMAKE_BUILD_TYPE=RELEASE \
            -D CMAKE_INSTALL_PREFIX=/usr/local \
            -D BUILD_SHARED_LIBS=NO \
            # -D WITH_FFMPEG=NO \
            # -D WITH_IPP=NO \
            # -D WITH_OPENEXR=NO \
            . && \
        make VERBOSE=1 && \
        make && \
        make install && \
        ln -s /usr/local/lib/python2.7/site-packages/cv2.so /usr/lib/python2.7/site-packages/cv2.so && \
        rm -rf /opt && \
        apk --no-cache add --virtual .rundeps \
            libjpeg \
            libjpeg-turbo \
            libpng \
            tiff \
            libwebp \
            libtbb \
            libjasper && \
        apk del .builddeps
