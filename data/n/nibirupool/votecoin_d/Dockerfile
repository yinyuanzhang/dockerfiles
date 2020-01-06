from ubuntu:latest
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y software-properties-common && \
  apt-get install -y curl vim wget git && \
  apt-get install -y libc6-dev g++-multilib python pwgen
RUN \
  apt-get install -y build-essential pkg-config libcurl3-gnutls-dev libc6-dev libevent-dev m4 g++-multilib autoconf libtool ncurses-dev unzip git python zlib1g-dev wget bsdmainutils automake libboost-all-dev libssl-dev libprotobuf-dev protobuf-compiler libqt4-dev libqrencode-dev libdb++-dev
WORKDIR /root
RUN \
wget https://github.com/Tomas-M/VoteCoin/releases/download/v1.1.2.1/VoteCoin-v1.1.2.1-Linux.tar.gz &&\
tar xzf VoteCoin-v1.1.2.1-Linux.tar.gz
COPY ./blocknotify.c /var/
RUN wget https://raw.githubusercontent.com/Tomas-M/VoteCoin/master/zcutil/fetch-params.sh && chmod +x ./fetch-params.sh 
RUN cd /var && gcc blocknotify.c -o blocknotify && mv /var/blocknotify /bin && rm /var/blocknotify.c
RUN \
  echo "#!/bin/bash\n/root/fetch-params.sh\n/root/VoteCoin-v1.1.2.1-Linux/votecoind ; bash" > /root/entry.sh &&\
  chmod +x /root/entry.sh
VOLUME ["/root/.votecoin"]
ADD ./votecoin.conf /root/.votecoin/votecoin.conf
ENTRYPOINT ["/root/entry.sh"]
#ENTRYPOINT ["bash"]
