FROM node:10-stretch

RUN apt-get update

#Install Google Chrome
RUN wget --quiet https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb || apt-get -qq install -y -f
RUN dpkg -i google-chrome-stable_current_amd64.deb

#Install Openjdk 8
RUN apt-get install default-jre -y
RUN apt-get install default-jdk -y

COPY . .
COPY java_test.sh /usr/local/bin
COPY chrome_test.sh /usr/local/bin
CMD java -version && google-chrome --version
