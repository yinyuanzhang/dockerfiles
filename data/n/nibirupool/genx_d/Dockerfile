from nibirupool/nibiru:latest
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install nano
RUN \
  wget http://de.archive.ubuntu.com/ubuntu/pool/universe/libs/libsodium/libsodium-dev_1.0.13-1_amd64.deb &&\
  wget http://de.archive.ubuntu.com/ubuntu/pool/universe/libs/libsodium/libsodium18_1.0.13-1_amd64.deb &&\
  dpkg -i libsodium*deb
RUN git clone https://github.com/genesisofficial/genesis.git
RUN  \
  cd genesis &&\
  ./autogen.sh &&\
  ./configure --disable-bench --disable-tests &&\
  make
COPY ./blocknotify.c /var/
RUN cd /var && gcc blocknotify.c -o blocknotify && mv /var/blocknotify /bin && rm /var/blocknotify.c
RUN \
  mkdir /root/.genesis && \
  echo "#!/bin/bash\n/genesis/src/genesisd && bash" > /root/entry.sh &&\
  chmod +x /root/entry.sh
ADD ./genesis.conf /root/.genesis/genesis.conf
VOLUME ["/root/.genesis"]
ENTRYPOINT ["/root/entry.sh"]
#ENTRYPOINT ["/bin/bash"]
