FROM debian

WORKDIR /tmp
EXPOSE 9223

RUN useradd -m chrome

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y xvfb

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN apt-get install -y gconf-service
RUN apt-get install -y libasound2
RUN apt-get install -y libatk1.0-0
RUN apt-get install -y libcairo2
RUN apt-get install -y libcups2
RUN apt-get install -y libfontconfig1
RUN apt-get install -y libgdk-pixbuf2.0-0
RUN apt-get install -y libgtk2.0-0
RUN apt-get install -y libnspr4
RUN apt-get install -y libnss3
RUN apt-get install -y libpango1.0-0 libxss1 libxtst6 libappindicator1 libcurl3 xdg-utils
RUN apt-get install -y fonts-liberation
RUN apt-get install -y libgtk-3-0 lsb-release
RUN apt-get install -y libappindicator3-1

# use socat to redirect the 9222 port
RUN apt-get install -y socat

RUN dpkg -i /tmp/google-chrome-stable_current_amd64.deb
RUN rm -rf /tmp/*
RUN apt-get purge
RUN apt-get clean
RUN apt-get autoremove -y
ENV DISPLAY :1.0

COPY remote-user-data-dir /home/chrome/remote-user-data-dir
RUN chown -R chrome /home/chrome/remote-user-data-dir
RUN chmod --recursive +rw /home/chrome/remote-user-data-dir/Default/Cache
RUN chmod 770 /home/chrome/remote-user-data-dir/Default/Cache

COPY start.sh /home/chrome/

USER chrome
WORKDIR /home/chrome

ENTRYPOINT ["sh", "/home/chrome/start.sh"]
