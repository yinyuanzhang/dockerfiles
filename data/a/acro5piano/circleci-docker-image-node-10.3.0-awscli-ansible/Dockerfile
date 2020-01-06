FROM circleci/node:10.3.0

USER circleci
WORKDIR /home/circleci

RUN echo 'deb http://ftp.de.debian.org/debian testing main' | sudo tee -a /etc/apt/sources.list
RUN sudo apt-get -y update
RUN sudo apt-get -y -t testing install python3.6 python3-pip  python3-dev

RUN sudo pip3 install -U setuptools pip
RUN sudo pip3 install awscli ansible

CMD ['bash']
