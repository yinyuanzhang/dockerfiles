FROM ubuntu:bionic
# prepare packages
RUN apt-get update \
&& apt-get -y upgrade \
&& export DEBIAN_FRONTEND=noninteractive \
&& apt-get -y install libboost-all-dev libdb4.8 libdb4.8++ libssl-dev unzip \
libevent-dev software-properties-common \
git build-essential libtool autotools-dev automake pkg-config bsdmainutils python3 \
libcap-dev libseccomp-dev zlib1g-dev wget libzmq3-dev libminiupnpc-dev \
&& apt-get -y install unzip \
&& apt-get -y install wget libzmq5 libminiupnpc10 libcap2

# prepare git
ENV GIT_COIN_URL https://github.com/Actinium-project/Actinium-ng.git
ENV GIT_COIN_NAME actinium-ng
# clone & compile
RUN	git clone $GIT_COIN_URL $GIT_COIN_NAME \
&& cd $GIT_COIN_NAME \
&& git checkout v0.19.0.4 \
&& chmod +x contrib/install_db4.sh \
&& chmod +x autogen.sh \
&& chmod +x share/genbuild.sh \
&& chmod +x src/leveldb/build_detect_platform \
&& ./contrib/install_db4.sh `pwd` \
&& export BDB_PREFIX=`pwd`/db4 \
&& ./autogen.sh && ./configure LDFLAGS="-L${BDB_PREFIX}/lib -ldb_cxx-4.8" CPPFLAGS="-I${BDB_PREFIX}/include" --disable-shared --disable-tests --disable-bench --without-gui LIBS="-lcap -lseccomp" \
&& make \
&& make install \
&& cd / && rm -rf /$GIT_COIN_NAME \
# switch to home dir
RUN mkdir /data
ENV HOME /data
#rpc port & main port
EXPOSE 4334 2300
# prepare daemon config file
COPY start.sh /start.sh
COPY genconf.sh /genconf.sh
RUN chmod 777 /*.sh
CMD /start.sh Actinium.conf ACM Actiniumd