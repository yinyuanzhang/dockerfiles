FROM profideo/php72-apache

RUN apt-get update && apt-get install -y unzip wget

RUN docker-php-ext-install pcntl

RUN apt-get update && apt-get install -y fonts-liberation libappindicator3-1 libnspr4 libnss3 libx11-xcb1 libxss1 libxtst6 xdg-utils lsb-release
COPY files/google-chrome-stable_72_amd64.deb /tmp/google-chrome-stable_72_amd64.deb
RUN dpkg -i /tmp/google-chrome-stable_72_amd64.deb
RUN rm /tmp/google-chrome-stable_72_amd64.deb

COPY files/install-java.sh /tmp/install-java.sh
# JDK is stored in static.profideo.com because it cannot be downloaded from official repository without authentication and
# it cannot be versionned because its size is too large.
RUN wget http://static.profideo.com/it/jdk-8u211-linux-x64.tar.gz -O /tmp/jdk-8u211-linux-x64.tar.gz
RUN chmod u+x /tmp/install-java.sh
RUN yes | /tmp/install-java.sh -f /tmp/jdk-8u211-linux-x64.tar.gz
RUN rm /tmp/install-java.sh
RUN rm /tmp/jdk-8u211-linux-x64.tar.gz

ADD https://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip /tmp/
RUN unzip -d /opt/ /tmp/chromedriver_linux64.zip
RUN rm /tmp/chromedriver_linux64.zip

ADD http://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar /opt/selenium-server-standalone.jar
RUN chmod o+r /opt/selenium-server-standalone.jar
