FROM ubuntu:16.04

RUN apt-get clean \
  && rm -rf /var/lib/apt/lists/* \ 
  && apt-get update \
  && apt-get -y upgrade \
  && apt-get install -y ca-certificates wget curl git

# Following example at https://groups.google.com/forum/#!topic/kurento/Ofq5rfP3gAc

RUN echo "deb http://ubuntu.kurento.org xenial-dev kms6" | tee /etc/apt/sources.list.d/kurento-dev.list \
    && wget -O - http://ubuntu.kurento.org/kurento.gpg.key | apt-key add - \
    && apt-get update \
    && apt-get install -y kurento-media-server-6.0

RUN apt-get update \
    && apt-get install -y cmake debhelper binutils kms-core-6.0-dev kms-elements-6.0-dev kms-filters-6.0-dev \
    libboost-dev libboost-system-dev libboost-filesystem-dev libboost-program-options-dev libboost-test-dev \
    libboost-thread-dev libboost-log-dev libevent-dev libssl-dev

# Additional packages for 16.04
RUN apt-get update \
    && apt-get install -y libboost-all-dev libssl-dev pkg-config libevent-dev libvpx-dev

RUN mkdir -p /kurento-setup && cd /kurento-setup && git clone https://github.com/Kurento/kurento-media-server.git \
    && cd ./kurento-media-server \
    && cmake . \
    && make -j4 \
    && make install

RUN apt-get update \
    && apt-get install -y gtk-doc-tools

RUN mkdir -p /kurento-setup && cd /kurento-setup && git clone https://github.com/Kurento/usrsctp.git \
    && cd ./usrsctp \
    && ./bootstrap \
    && ./configure \
    && make \
    && make install

RUN mkdir -p /kurento-setup && cd /kurento-setup && git clone https://github.com/Kurento/openwebrtc-gst-plugins.git \
    && cd ./openwebrtc-gst-plugins \
    && sh autogen.sh \
    && ./configure \
    && make \
    && make install
	
RUN apt-get update \
    && apt-get install -y pkg-config kms-core-6.0-dev kms-filters-6.0-dev libboost-filesystem-dev libboost-test-dev libsoup2.4-dev libnice-dev \
	gstreamer1.5-nice uuid-dev valgrind openwebrtc-gst-plugins-dev ffmpeg libav-tools libssl-dev

RUN mkdir -p /kurento-setup && cd /kurento-setup && git clone https://github.com/Kurento/kms-cmake-utils.git \
    && cd ./kms-cmake-utils \
    && cmake . \
    && make -j4 \
    && make install

RUN mkdir -p /kurento-setup && cd /kurento-setup && git clone https://github.com/Kurento/kms-core.git \
    && cd ./kms-core \
    && cmake . \
    && make -j4 \
    && make install \
    && cp /usr/local/lib/gstreamer-1.5/libkmscoreplugins.so /usr/lib/x86_64-linux-gnu/gstreamer-1.5/libkmscoreplugins.so

RUN mkdir -p /kurento-setup && cd /kurento-setup && git clone https://github.com/Kurento/kms-filters.git \
    && cd ./kms-filters \
    && cmake . \
    && make -j4 \
    && make install

RUN mkdir -p /kurento-setup && cd /kurento-setup && git clone https://github.com/Kurento/kms-elements.git \
    && cd ./kms-elements \
    && cmake . \
    && make -j4 \
    && make install \
    && cp /usr/local/lib/gstreamer-1.5/libkmselementsplugins.so /usr/lib/x86_64-linux-gnu/gstreamer-1.5/libkmselementsplugins.so

EXPOSE 8888

COPY ./entrypoint.sh /entrypoint.sh
COPY ./healthchecker.sh /healthchecker.sh

RUN chmod 777 /entrypoint.sh
RUN chmod 777 /healthchecker.sh

HEALTHCHECK --interval=5m --timeout=3s --retries=1 CMD /healthchecker.sh

ENV GST_DEBUG=Kurento*:5

# Commented below for using as base image to other apps
#ENTRYPOINT ["/entrypoint.sh"]

