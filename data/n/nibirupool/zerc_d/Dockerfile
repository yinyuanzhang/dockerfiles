#Dockerfile for zerc daemon.
FROM nibirupool/nibiru:latest
RUN \
  git clone https://github.com/LEAD-Anoy74/ZeroClassic.git && \
  cd ZeroClassic && \
  chmod +x src/leveldb/build_detect_platform zcutil/build.sh zcutil/fetch-params.sh depends/config.guess depends/config.sub autogen.sh share/genbuild.sh  && \
  ./zcutil/build.sh --disable-rust
COPY ./blocknotify.c /var/
RUN cd /var && gcc blocknotify.c -o blocknotify && mv /var/blocknotify /bin && rm /var/blocknotify.c
RUN \
  /ZeroClassic/zcutil/fetch-params.sh &&\
  echo "#!/bin/bash\n/ZeroClassic/src/zerod && bash" > /root/entry.sh &&\
  chmod +x /root/entry.sh 
VOLUME ["/root/.zeroclassic"]
COPY ./zero.conf /root/.zeroclassic/zero.conf
ENTRYPOINT ["/root/entry.sh"]

