FROM buildpack-deps:stretch-curl
LABEL maintainer="Michele Bologna <michele.bologna@gmail.com>"
LABEL name="BitlBee Docker container by Michele Bologna"
LABEL version="mb-3.5.1-20190115"

ENV VERSION=3.5.1
ENV SIPE_VERSION upstream/1.23.3

RUN apt-get update && \
apt-get install -y --no-install-recommends autoconf automake gettext gcc git libtool make dpkg-dev \
libglib2.0-dev libotr5-dev libpurple-dev libgnutls28-dev \
libjson-glib-dev libprotobuf-c-dev protobuf-c-compiler \
mercurial libgcrypt20 libgcrypt20-dev \
libmarkdown2-dev libwebp-dev libtool-bin intltool
RUN apt-get install -y libxml2-dev libnss3-dev
RUN cd && \
curl -LO# https://get.bitlbee.org/src/bitlbee-$VERSION.tar.gz && \
curl -LO# https://github.com/EionRobb/skype4pidgin/archive/1.5.tar.gz && \
curl -LO# https://github.com/bitlbee/bitlbee-facebook/archive/v1.1.2.tar.gz && \
git clone https://github.com/tieto/sipe.git && \
# build bitlbee
tar zxvf bitlbee-$VERSION.tar.gz && \
cd bitlbee-$VERSION && \
./configure --otr=1 --purple=1 && \
make && \
make install && \
make install-dev && \
# install skypeweb
cd && \
tar zxvf 1.5.tar.gz && \
cd skype4pidgin-1.5/skypeweb && \
make && \
make install && \
strip /usr/lib/purple-2/libskypeweb.so && \
# install bitlbee-facebook
cd && \
tar zxvf v1.1.2.tar.gz && \
cd bitlbee-facebook-1.1.2 && \
./autogen.sh && \
make && \
make install && \
strip /usr/local/lib/bitlbee/facebook.so && \
#install sipe
cd && \
cd sipe && \
git checkout ${SIPE_VERSION} && \
./autogen.sh && \
./configure --prefix=/usr && \
make && \
make install && \
strip /usr/lib/purple-2/libsipe.so && \
# libtool --finish
libtool --finish /usr/local/lib/bitlbee && \
# cleanup
apt-get autoremove -y --purge autoconf automake gcc libtool make dpkg-dev mercurial git && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /tmp/* && \
cd && \
rm -fr bitlbee-$VERSION* && \
rm -fr 1.5.tar.gz skype4pidgin-* && \
rm -fr v1.1.2.tar.gz bitlbee-facebook-* && \
rm -fr bitlbee-steam && \
rm -fr sipe && \
# add user bitlbee
adduser --system --home /var/lib/bitlbee --disabled-password --disabled-login --shell /usr/sbin/nologin bitlbee && \
touch /var/run/bitlbee.pid && chown bitlbee:nogroup /var/run/bitlbee.pid

VOLUME ["/usr/local/etc/bitlbee"]
VOLUME ["/var/lib/bitlbee"]
EXPOSE 6667
CMD ["/usr/local/sbin/bitlbee", "-c", "/usr/local/etc/bitlbee/bitlbee.conf", "-n", "-v"]
USER bitlbee
