FROM debian:8.10

RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list
COPY linux_signing_key.pub /tmp/linux_signing_key.pub
RUN apt-key add /tmp/linux_signing_key.pub

RUN apt-get update
RUN apt-get install -y firefox-esr google-chrome-stable


RUN useradd -u 1000 worker
RUN mkdir /home/worker; chown worker:worker /home/worker
RUN echo "worker:password" | chpasswd

COPY startit.sh /tmp/

CMD ["/tmp/startit.sh"]
