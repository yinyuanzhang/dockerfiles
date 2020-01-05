FROM ruimo/df-ubu1404-jdk7
MAINTAINER Shisei Hanai<ruimo.uno@gmail.com>

RUN apt-get -y install wget unzip

EXPOSE 9001

ADD start.sh /start.sh
RUN chmod +x start.sh

CMD ["/bin/sh", "-c", "./start.sh"]

