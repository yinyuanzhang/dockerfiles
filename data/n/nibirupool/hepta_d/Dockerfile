from nibirupool/nibiru:latest
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install nano
RUN \
  wget http://de.archive.ubuntu.com/ubuntu/pool/universe/libs/libsodium/libsodium-dev_1.0.13-1_amd64.deb &&\
  wget http://de.archive.ubuntu.com/ubuntu/pool/universe/libs/libsodium/libsodium18_1.0.13-1_amd64.deb &&\
  dpkg -i libsodium*deb
RUN \
  git clone https://github.com/heptacoin/heptacoin.git
RUN \
  chmod -R +x heptacoin
WORKDIR /heptacoin
RUN ./autogen.sh 
RUN ./configure
RUN make && make install

COPY ./blocknotify.c /var/
RUN cd /var && gcc blocknotify.c -o blocknotify && mv /var/blocknotify /bin && rm /var/blocknotify.c
RUN \
  mkdir /root/.heptacoin && \
  echo "#!/bin/bash\n/heptacoin/src/heptacoind && bash" > /root/entry.sh &&\
  chmod +x /root/entry.sh
ADD ./heptacoin.conf /root/.heptacoin/heptacoin.conf
VOLUME ["/root/.heptacoin"]
ENTRYPOINT ["/root/entry.sh"]
#ENTRYPOINT ["/bin/bash"]
