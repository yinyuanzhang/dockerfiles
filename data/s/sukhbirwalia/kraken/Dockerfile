FROM ampush/base-pyservice:v7_p3.6


RUN apt-get --purge autoremove -y python3-setuptools python3-dev python3-pip
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get update
RUN apt-get install -y python3-setuptools
RUN apt-get install -y python3-dev
RUN apt-get install -y git
RUN apt-get install -y libmariadbclient-dev
RUN apt-get install -y default-libmysqlclient-dev

RUN curl https://bootstrap.pypa.io/get-pip.py | python3

RUN rm -rf /var/lib/apt/lists/*
RUN apt-get clean
RUN apt-get update
# We need wget to set up the PPA and xvfb to have a virtual screen and unzip to install the Chromedriver
RUN apt-get -qq -y install wget xvfb unzip libdbus-glib-1-2

RUN curl https://bootstrap.pypa.io/get-pip.py | python3

# Set the project name
ENV PROJECT_NAME="kraken"

# Copy over the source
RUN mkdir -p /code/$PROJECT_NAME

WORKDIR /code/$PROJECT_NAME

ADD ./requirements.txt /code/$PROJECT_NAME/requirements.txt

# Install the requirements.txt
RUN yes | pip3 install -r requirements.txt

# ADD the app#
ADD . /code/$PROJECT_NAME

ADD config /config/

# Exposing your app port
EXPOSE 80

RUN apt-get clean
RUN cp -r /var/lib/apt/lists /var/lib/apt/lists.old
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get clean

RUN dpkg -C
RUN apt-mark showhold
RUN dpkg --audit
RUN cp /etc/apt/sources.list /etc/apt/sources.list_backup
RUN sed -i s/stretch/buster/g /etc/apt/sources.list

RUN apt list --upgradable

# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'


RUN apt-get clean
RUN cp -r /var/lib/apt/lists /var/lib/apt/lists.old
RUN rm -rf /var/lib/apt/lists/*/*
RUN apt-get clean
RUN apt-get update

# Update the package list and install chrome
RUN apt-get install -y google-chrome-stable

 # Set up Chromedriver Environment variables
ENV CHROMEDRIVER_VERSION 76.0.3809.68
ENV CHROMEDRIVER_DIR /chromedriver
RUN mkdir $CHROMEDRIVER_DIR

 # Download and install Chromedriver
RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR

 # Put Chromedriver into the PATH
ENV PATH $CHROMEDRIVER_DIR:$PATH
 RUN mv $CHROMEDRIVER_DIR/chromedriver /usr/local/bin
 RUN chmod a+x /usr/local/bin/chromedriver

#Install FF
RUN wget https://ftp.mozilla.org/pub/firefox/releases/58.0/linux-x86_64/en-US/firefox-58.0.tar.bz2
RUN tar -xjf firefox-58.0.tar.bz2
RUN mv firefox /opt/firefox58
RUN ln -s /opt/firefox58/firefox-bin /usr/local/bin/firefox


# Download and install GeckoDriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz
RUN tar -xvzf geckodriver-v0.20.1-linux64.tar.gz
RUN rm geckodriver-v0.20.1-linux64.tar.gz
RUN chmod +x geckodriver
RUN mv geckodriver /usr/local/bin/
ENV PATH $(pwd):$PATH

#enable the browser display and in case we need to take screenshots

RUN Xvfb :99 -ac -screen 0 1280x1024x24 &
RUN nice -n 10 x11vnc 2>&1 &


CMD ["/usr/local/bin/dumb-init",  "/usr/local/bin/start.sh"]
