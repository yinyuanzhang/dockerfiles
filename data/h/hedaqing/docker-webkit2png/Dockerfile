FROM phusion/baseimage:latest

# Setup timezone
RUN echo Asia/Shanghai > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

# Install X, python, apache2 and php5
RUN apt-get update ; apt-get install -y xorg openbox xvfb xbase-clients xfonts-base libgtk2.0-0 xfonts-wqy libapache2-mod-php5 php5-curl python-qt4 libqt4-webkit python-pip python-setuptools git-core

# Install webkit2png

#use source, due to the bug https://github.com/adamn/python-webkit2png/issues/42
#RUN pip install webkit2png 

RUN git clone git://github.com/adamn/python-webkit2png.git ; cd python-webkit2png ; python setup.py install ; cd .. ; rm -rf python-webkit2png

# Install url2png.php
ADD app/*.php /var/www/html/

# Startup X
RUN mkdir /etc/service/xserver
ADD services/xserver.sh /etc/service/xserver/run
RUN chmod +x /etc/service/xserver/run

# Startup Apache
RUN mkdir /etc/service/apache2
ADD services/apache2.sh /etc/service/apache2/run
RUN chmod +x /etc/service/apache2/run

# Allow visit HTTP
EXPOSE 80

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
