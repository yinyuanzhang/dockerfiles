#===========================================================
# libnserial arm build (SerialPortStream)
# https://github.com/jcurl/SerialPortStream
#===========================================================
FROM resin/raspberrypi3-debian

RUN [ "cross-build-start" ]

# install required build tools.
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils build-essential cmake gcc git make

# clone the driver repo and build.
WORKDIR /usr/src
RUN git clone --no-checkout https://github.com/jcurl/serialportstream.git
WORKDIR /usr/src/serialportstream
RUN git checkout d25bbf9f9d2f4f32e9f324b23771257d7e4b97d6
WORKDIR /usr/src/serialportstream/dll/serialunix

# build the driver.
RUN ./build.sh

# make sure the target directory exists
WORKDIR /opt/

# copy the final file to the output directory
RUN cp /usr/src/serialportstream/dll/serialunix/bin/usr/local/lib/libnserial.so.1.1 /opt/libnserial.so.1.1

RUN [ "cross-build-end" ]
