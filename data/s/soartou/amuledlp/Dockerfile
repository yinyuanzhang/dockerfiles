FROM ubuntu:bionic

RUN apt update && \
    apt install -y libcrypto++ libwxgtk3.0 sudo
 
ADD  amule-dlp_2.3.2-1_amd64.deb /tmp
RUN  dpkg -i /tmp/amule-dlp_2.3.2-1_amd64.deb && \
     rm /tmp/amule-dlp_2.3.2-1_amd64.deb
ADD  libantiLeech.so /usr/share/amule/
ADD amule.sh /home/amule/amule.sh
RUN chmod a+x /home/amule/amule.sh 

EXPOSE 4711/tcp 4712/tcp 4672/udp 4665/udp 4662/tcp 4661/tcp
ENTRYPOINT ["/home/amule/amule.sh"]

