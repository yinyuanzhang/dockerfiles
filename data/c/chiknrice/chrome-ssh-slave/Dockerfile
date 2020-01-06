# chrome-ssh-slave
# Copyright (C) 2019 chiknrice 
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

FROM jenkins/ssh-slave

# Install xvfb, chrome and chromedriver
ARG CHROME_VERSION="google-chrome-stable"

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
  apt-get update -y && \
  apt-get -y install xvfb ${CHROME_VERSION:-google-chrome-stable} && \
  rm /etc/apt/sources.list.d/google-chrome.list && \
  rm -rf /var/lib/apt/lists/* /var/cache/apt/* && \
  CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
  mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
  curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
  unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
  rm /tmp/chromedriver_linux64.zip && \
  chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
  ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver
  
ENV DISPLAY :99

# Copy start-slave wrapper script
COPY files/start-slave.sh /usr/local/bin/start-slave.sh
RUN chmod a+rx /usr/local/bin/start-slave.sh

ENTRYPOINT ["start-slave.sh"]

