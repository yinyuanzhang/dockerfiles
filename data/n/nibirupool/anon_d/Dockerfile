#Dockerfile for anon daemon.
FROM nibirupool/nibiru:latest
WORKDIR /root
RUN \
  git clone https://github.com/anonymousbitcoin/anon.git anon
RUN \
   chmod +x /root/anon/anonutil/build.sh
RUN \
   bash /root/anon/anonutil/build.sh
   RUN export OSTYPE="linux-gnu"
COPY ./blocknotify.c /var/
RUN cd /var && gcc blocknotify.c -o blocknotify && mv /var/blocknotify /bin && rm /var/blocknotify.c
RUN \
  mkdir /root/.anon
RUN \
  echo "#!/bin/bash\nbash /root/anon/anonutil/fetch-params.sh\n/anon/src/anond && bash" > /root/entry.sh &&\
  chmod +x /root/entry.sh
VOLUME ["/root/.anon"]
ADD ./anon.conf /root/.anon/anon.conf
ENTRYPOINT ["./root/entry.sh"]
#ENTRYPOINT ["bash"]