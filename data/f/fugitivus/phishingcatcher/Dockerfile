#ubuntu docker-container for general purpose:
#build with docker build -f ubuntu.docker -t fugitivus/ubuntu:latest .

FROM fugitivus/ubuntu:xenial
MAINTAINER fugitivus <fugitivus@gmx.de>

#environment-variables for non-interactive shell:
#ENV DEBIAN_FRONTEND noninteractive

#install updates, some packages and do cleanup:
RUN apt-get update && apt-get upgrade -y\
 && apt-get install apt-utils python python-pip git -y\
 && apt-get install net-tools htop bmon joe aptitude -y\
 && git clone https://github.com/x0rz/phishing_catcher.git\
 && cd phishing_catcher\
 && pip install -r requirements.txt\
#show usage each time attaching container:
 && echo "echo -e -n '\033[1;33m'" >> /etc/bash.bashrc\
 && echo "echo 'To run phishing_catcher, type:'" >> /etc/bash.bashrc\
 && echo "echo -e -n '\033[0m'" >> /etc/bash.bashrc\
 && echo "echo 'cd phishing_catcher'" >> /etc/bash.bashrc\
 && echo "echo './catch_phishing.py'" >> /etc/bash.bashrc\
#do some cleanup:
 && apt-get clean autoclean\
 && apt-get autoremove -y\
 && rm -rf /var/lib/{apt,dpkg,cache,log}/
