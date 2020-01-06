#Dockerfile for zen daemon.
FROM nibirupool/nibiru:latest
RUN \
  git clone https://github.com/ZencashOfficial/zen.git && \
  cd zen && ./zcutil/build.sh
COPY ./blocknotify.c /var/
RUN cd /var && gcc blocknotify.c -o blocknotify && mv /var/blocknotify /bin && rm /var/blocknotify.c
RUN \
  /zen/zcutil/fetch-params.sh &&\
  echo "#!/bin/bash\n/zen/src/zend && bash" > /root/entry.sh &&\
  chmod +x /root/entry.sh 
VOLUME ["/root/.zen"]
COPY ./zen.conf /root/.zen/zen.conf
ENTRYPOINT ["/root/entry.sh"]

