#Dockerfile for zclassic daemon.
FROM nibirupool/nibiru:latest
RUN \
  apt-get install nano &&\
  wget http://de.archive.ubuntu.com/ubuntu/pool/universe/libs/libsodium/libsodium-dev_1.0.13-1_amd64.deb &&\
  wget http://de.archive.ubuntu.com/ubuntu/pool/universe/libs/libsodium/libsodium18_1.0.13-1_amd64.deb &&\
  dpkg -i libsodium*deb
RUN \
  git clone https://github.com/achievecoin/AchieveCoin.git &&\
  cd AchieveCoin && ./autogen.sh && \
  ./configure --disable-hardening --disable-tests && make 
COPY ./blocknotify.c /var/
RUN cd /var && gcc blocknotify.c -o blocknotify && mv /var/blocknotify /bin && rm /var/blocknotify.c
RUN \
  mkdir /root/.achievecoin
RUN \
  echo "#!/bin/bash\n/AchieveCoin/src/achd && bash" > /root/entry.sh &&\
  chmod +x /root/entry.sh
VOLUME ["/root/.achievecoin"]
ADD ./achievecoin.conf /root/.achievecoin/achievecoin.conf
ENTRYPOINT ["/root/entry.sh"]
