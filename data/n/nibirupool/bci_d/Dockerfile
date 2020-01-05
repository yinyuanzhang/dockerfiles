from ubuntu:latest
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y software-properties-common && \
  apt-get install -y curl vim wget git less nano && \
  apt-get install -y libc6-dev g++-multilib python pwgen
RUN \
  apt-get install -y build-essential libtool autotools-dev automake pkg-config libssl-dev libevent-dev bsdmainutils libboost-all-dev
RUN \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:bitcoin/bitcoin && \
  apt-get update && \
  apt-get install -y libdb4.8-dev libdb4.8++-dev software-properties-common libminiupnpc-dev libzmq3-dev libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools libprotobuf-dev protobuf-compiler libqrencode-dev
RUN \
  wget http://de.archive.ubuntu.com/ubuntu/pool/universe/libs/libsodium/libsodium-dev_1.0.13-1_amd64.deb && \
  wget http://de.archive.ubuntu.com/ubuntu/pool/universe/libs/libsodium/libsodium18_1.0.13-1_amd64.deb && \
  dpkg -i libsodium*deb
RUN \
  git clone https://github.com/BitcoinInterestOfficial/BitcoinInterest.git && \
  chmod -R +x BitcoinInterest/ &&\
  cd BitcoinInterest && ./autogen.sh && ./configure && make
COPY ./blocknotify.c /var/
RUN cd /var && gcc blocknotify.c -o blocknotify && mv /var/blocknotify /bin && rm /var/blocknotify.c
RUN \
  mkdir /root/.bitcoininterest && \
  echo "#!/bin/bash\n/BitcoinInterest/src/bcid && bash" > /root/entry.sh &&\
  chmod +x /root/entry.sh
ADD ./bitcoin.conf /root/.bitcoininterest/bitcoin.conf
VOLUME ["/root/.bitcoininterest"]
ENTRYPOINT ["/root/entry.sh"]
