FROM profideo/php71-nginx

RUN apt-get update && apt-get install -y unzip wget

RUN docker-php-ext-install pcntl

RUN echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN apt-get update && apt-get install -y google-chrome-stable

COPY files/install-java.sh /tmp/install-java.sh
# JDK is stored in static.profideo.com because it cannot be downloaded from official repository without authentication and
# it cannot be versionned because its size is too large.
RUN wget http://static.profideo.com/it/jdk-8u211-linux-x64.tar.gz -O /tmp/jdk-8u211-linux-x64.tar.gz
RUN chmod u+x /tmp/install-java.sh
RUN yes | /tmp/install-java.sh -f /tmp/jdk-8u211-linux-x64.tar.gz
RUN rm /tmp/install-java.sh
RUN rm /tmp/jdk-8u211-linux-x64.tar.gz

ADD https://chromedriver.storage.googleapis.com/2.38/chromedriver_linux64.zip /tmp/
RUN unzip -d /opt/ /tmp/chromedriver_linux64.zip
RUN rm /tmp/chromedriver_linux64.zip

ADD https://selenium-release.storage.googleapis.com/3.12/selenium-server-standalone-3.12.0.jar /opt/selenium-server-standalone.jar
RUN chmod o+r /opt/selenium-server-standalone.jar
