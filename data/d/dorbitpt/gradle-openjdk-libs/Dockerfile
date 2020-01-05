FROM dorbitpt/gradle-openjdk:4.10.3

ARG DOWNLOAD_PATH=~/Downloads

# Install libs
RUN apt-get update \
    && apt-get -y install liblzo2-2 \
    && apt-get -y install liblzo2-dev \
    && apt-get -y install libgpg-error0 \
    && apt-get -y install libgpg-error-dev \
    && apt-get -y install zlib1g \
    && apt-get -y install zlib1g-dev 

# Download and install the LIBGCRYPT (from Gnu Privacy Guard) encryption library
ARG LIBGCRYPT_NAME=libgcrypt
ARG LIBGCRYPT_VERSION=1.8.4
ARG LIBGCRYPT_EXTENSION=tar.bz2
ARG LIBGCRYPT_LINK=https://www.gnupg.org/ftp/gcrypt/libgcrypt/${LIBGCRYPT_NAME}-${LIBGCRYPT_VERSION}.${LIBGCRYPT_EXTENSION}
RUN wget ${LIBGCRYPT_LINK} -P ${DOWNLOAD_PATH} \
&& tar -xf ${DOWNLOAD_PATH}/${LIBGCRYPT_NAME}-${LIBGCRYPT_VERSION}.${LIBGCRYPT_EXTENSION} -C ${DOWNLOAD_PATH} \
&& cd ${DOWNLOAD_PATH}/${LIBGCRYPT_NAME}-${LIBGCRYPT_VERSION} \
&& ./configure \
&& make \
&& make install