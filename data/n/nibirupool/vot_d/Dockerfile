#Dockerfile for Votecoin daemon.
FROM nibirupool/nibiru:latest
RUN \
  git clone https://github.com/Tomas-M/VoteCoin.git &&\
  cd VoteCoin && ./zcutil/votecoin_build_debian.sh
COPY ./blocknotify.c /var/
RUN cd /var && gcc blocknotify.c -o blocknotify && mv /var/blocknotify /bin && rm /var/blocknotify.c
RUN \
  /VoteCoin/zcutil/fetch-params.sh &&\
  echo "#!/bin/bash\n/VoteCoin/src/votecoind && bash" > /root/entry.sh &&\
  chmod +x /root/entry.sh 
VOLUME ["/root/.votecoin"]
COPY ./votecoin.conf /root/.votecoin/votecoin.conf
ENTRYPOINT ["/root/entry.sh"]
