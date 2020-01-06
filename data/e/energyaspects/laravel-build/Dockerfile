FROM circleci/php:7.1-jessie-node-browsers

RUN sudo apt-get update \
    && sudo apt-get upgrade \
    && sudo apt-get install zlib1g-dev libsqlite3-dev tar gzip libyaml-dev libcurl3

RUN sudo docker-php-ext-install zip bcmath pdo pdo_mysql

RUN sudo apt install python3 python3-venv python3-pip python3-yaml python3-socksipy build-essential
RUN sudo pip3 install awscli
RUN sudo pip3 install awsebcli --upgrade
RUN sudo pip3 install --upgrade pip setuptools wheel
RUN sudo pip3 install pandas --upgrade


RUN sudo curl -L https://github.com/docker/compose/releases/download/1.23.2/docker-compose-`uname -s`-`uname -m` > ~/docker-compose \
    && sudo chmod +x ~/docker-compose \
    && sudo mv ~/docker-compose /usr/local/bin/docker-compose
