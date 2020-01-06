FROM ubuntu

# Install nzbget
RUN apt-get update && apt-get install -y wget python unzip \
  && wget -O - http://nzbget.net/info/nzbget-version-linux.json | \     
     sed -n "s/^.*stable-download.*: \"\(.*\)\".*/\1/p" | \
     wget --no-check-certificate -i - -O nzbget-latest-bin-linux.run \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && apt-get autoremove -y && apt-get clean -y \
  && sh nzbget-latest-bin-linux.run && rm nzbget-latest-bin-linux.run

# Scripts
WORKDIR /nzbget/scripts

# Install subliminal
RUN wget https://github.com/caronc/nzb-subliminal/archive/master.zip \
  && unzip master.zip nzb-subliminal-master/Subliminal.py nzb-subliminal-master/Subliminal/* \
  && mv nzb-subliminal-master/* . \
  && rm -rf master.zip nzb-subliminal-master

# Install notify
RUN wget https://github.com/caronc/nzb-notify/archive/master.zip \
  && unzip master.zip nzb-notify-master/Notify.py nzb-notify-master/Notify/* \
  && mv nzb-notify-master/* . \
  && rm -rf master.zip nzb-notify-master

EXPOSE 6789

CMD if [ -e "/nzbget.conf" ]; then /nzbget/nzbget -s -c /nzbget.conf -o outputmode=log; else /nzbget/nzbget -s -o outputmode=log;touch /nzbget.conf;fi
