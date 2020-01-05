FROM ruby:2.2
MAINTAINER Erik Beltran - Joseph Paz
# Install Firefox
RUN update-ca-certificates --fresh
RUN curl 'https://download-installer.cdn.mozilla.net/pub/firefox/releases/35.0/linux-x86_64/en-US/firefox-35.0.tar.bz2' -o firefox.tar.bz2
RUN bunzip2 firefox.tar.bz2
RUN tar -xf firefox.tar
RUN rm firefox.tar
RUN apt-get update
RUN apt-get install -y xvfb libasound2 libgtk2.0-0 libdbus-glib-1-2 libxcomposite1
RUN mv /firefox /opt/
RUN ln -s /opt/firefox/firefox-bin /usr/bin/firefox
RUN firefox -v
#Siempre se debe dejar ejecutando un proceso

ADD start.sh start.sh
ENTRYPOINT ["/start.sh"]
ENV DISPLAY :1
RUN echo $DISPLAY

ADD test_webdriver.rb /tmp/test_webdriver.rb
RUN gem install selenium-webdriver
RUN xvfb-run ruby /tmp/test_webdriver.rb

CMD ["bash"]
