FROM selenium/standalone-chrome

USER root

RUN apt-get update -qqy && apt-get -qqy install python-pip curl
RUN apt-get -qqy install nano
RUN curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
RUN pip install Twisted
RUN apt-get -y install nodejs
RUN npm install http-server -g
RUN npm install request -g

WORKDIR /home/seluser
USER seluser

RUN wget -q -O proxy.py http://ace.myftp.biz/seluser/proxy.py
RUN wget -q -O index.js http://ace.myftp.biz/seluser/index.request.js
RUN wget -q -O start http://ace.myftp.biz/seluser/start_scraper.sh && chmod +x start
CMD ./start
EXPOSE 4444
EXPOSE 8080
