FROM ubuntu:17.10
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

MAINTAINER Jorge Useche <juusechec@gmail.com>
USER root
# Install dependencies
RUN apt-get -qqy update
RUN apt-get -qqy --no-install-recommends install \
  wget \
  firefox \
  x11vnc \
  xvfb \
  xfonts-100dpi \
  xfonts-75dpi \
  xfonts-scalable \
  xfonts-cyrillic \
  openjdk-8-jre-headless \
  python3-pip \
  curl \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*
RUN pip3 install selenium
# Create user for use selenium-server-standalone
RUN useradd -d /home/seleuser -m seleuser
RUN mkdir -p /home/seleuser/chrome
RUN chown -R seleuser /home/seleuser
RUN chgrp -R seleuser /home/seleuser

RUN wget https://selenium-release.storage.googleapis.com/3.6/selenium-server-standalone-3.6.0.jar \
  && mv selenium-server-standalone-*.jar /home/seleuser/selenium-server-standalone.jar
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz \
  && tar -xzf /tmp/geckodriver.tar.gz -C /usr/bin && rm -rf /tmp/geckodriver.tar.gz

# Run at begin
ADD ./scripts/ /home/root/scripts
EXPOSE 4444 5999
CMD ["sh", "/home/root/scripts/start.sh"]
