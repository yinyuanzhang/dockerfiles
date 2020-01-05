from nibirupool/nibiru:latest
RUN \
    git clone https://github.com/Snowgem/Snowgem.git &&\
    cd Snowgem &&\
    chmod +x zcutil/build.sh depends/config.guess depends/config.sub autogen.sh share/genbuild.sh src/leveldb/build_detect_platform depends/Makefile
RUN \
    cd Snowgem &&\
    ./zcutil/build.sh --disable-rust
RUN \
  cd Snowgem &&\
  chmod +x zcutil/fetch-params.sh &&\
  ./zcutil/fetch-params.sh &&\
  mkdir /root/.snowgem
RUN \
  echo "#!/bin/bash\n/Snowgem/src/snowgemd && bash" > /root/entry.sh &&\
  chmod +x /root/entry.sh
VOLUME ["/root/.snowgem"]
ADD ./snowgem.conf /root/.snowgem/snowgem.conf
ADD ./masternode.conf /root/.snowgem/masternode.conf
ENTRYPOINT ["/root/entry.sh"]

