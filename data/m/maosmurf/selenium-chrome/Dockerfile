FROM maosmurf/maven-3

# install
RUN apt-get -qq update
RUN apt-get -qqy install chromium-chromedriver xvfb unzip

# clean
RUN apt-get clean
RUN apt-get autoremove -yq
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Autostart Xvfb
COPY init.d.xvfb /etc/init.d/xvfb
RUN chmod 755 /etc/init.d/xvfb
RUN echo /etc/init.d/xvfb start >> /root/.profile
ENV DISPLAY :1

# get latest chromedriver
ENV LD_LIBRARY_PATH /usr/lib/chromium-browser/libs
RUN wget -q -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/2.14/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip -d /opt/chromedriver
RUN rm /tmp/chromedriver.zip
