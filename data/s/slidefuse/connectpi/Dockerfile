# docker run -d --name test -v /opt/vc:/opt/vc --device /dev/vchiq:/dev/vchiq --device /dev/fb0:/dev/fb0 --net host connect_image

FROM resin/armv7hf-debian-qemu
RUN [ "cross-build-start" ]

# Replace shell with bash so we can source files
#RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Set environment variables
ENV appDir /var/www/app/current

# Run updates and install deps
RUN apt-get update

RUN apt-get install -y -q --no-install-recommends \
    curl \
	git \
    liblockdev1 \
    udev \
    libxrandr2 \
	wget \
	ca-certificates \
	libpcre3 \
	libfreetype6 \
	fonts-freefont-ttf \
	dbus \
	libssl1.0.0 \
	libsmbclient \
	libssh-4 \
	fbset \
	lirc \
	inputlirc

#install libraspberrypi0
RUN wget http://mirrordirector.raspbian.org/raspbian/pool/firmware/r/raspberrypi-firmware-nokernel/raspberrypi-bootloader-nokernel_1.20150212-1~nokernel1_armhf.deb && dpkg -i raspberrypi-bootloader-nokernel_1.20150212-1~nokernel1_armhf.deb
RUN wget http://mirrordirector.raspbian.org/raspbian/pool/firmware/r/raspberrypi-firmware-nokernel/libraspberrypi0_1.20150212-1~nokernel1_armhf.deb && dpkg -i libraspberrypi0_1.20150212-1~nokernel1_armhf.deb

#install omx player
RUN wget https://archive.raspberrypi.org/debian/pool/main/o/omxplayer/omxplayer_0.3.6~git20160102~f544084_armhf.deb && dpkg -i omxplayer_0.3.6~git20160102~f544084_armhf.deb


RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -

RUN apt-get install -y -q nodejs

#clean up apt
RUN rm -rf /var/lib/apt/lists/* \
    && apt-get -y autoclean

# Set the work directory
RUN mkdir -p /var/www/app/current
WORKDIR ${appDir}

#install cec-client
RUN mkdir -p lib/
ADD ./pkg/libcec_20150809-1_armhf.deb .
RUN dpkg -i libcec_20150809-1_armhf.deb \
	&& ln -s /lib/arm-linux-gnueabihf/libudev.so.1 /lib/arm-linux-gnueabihf/libudev.so.0 \
	&& ldconfig
ADD ./lib/ /lib/arm-linux-gnueabihf/

#cleanup packages
RUN rm -f raspberrypi-bootloader-nokernel_1.20150212-1~nokernel1_armhf.deb libraspberrypi0_1.20150212-1~nokernel1_armhf.deb omxplayer_0.3.6~git20160102~f544084_armhf.deb libcec_20150809-1_armhf.deb

RUN npm install -g pm --unsafe-perm

# Add our package.json and install *before* adding our application files
ADD package.json ./
RUN npm i --production

ADD ./aminogfx-gl node_modules/aminogfx-gl

RUN npm cache clear

# Add application files
ADD . /var/www/app/current

# Cross build end for qemu-arm
RUN [ "cross-build-end" ]

CMD ["node_modules/pm2/bin/pm2-docker", "app.js"]


