FROM jenkins/ssh-slave

LABEL "org.label-schema.vendor"="OPOTEL Ltd" \
    version="1.0" \
    maintainer="dev@opotel.com" \
    description="Docker Jenkins Slave; Build, Test and Deploy Node.js + Python3 projects and build Docker images from Dockerfile"
# Python Version    
ARG ver=3.5  

#Install Docker
RUN curl -sSL https://get.docker.com/ | sh
RUN apt-get update && apt-get install -y \
    software-properties-common
    
RUN curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh && bash nodesource_setup.sh
RUN apt-get install -y nodejs   

RUN apt-get update \
    && apt-get dist-upgrade -y \
    && apt-get -y install python"${ver}" \
       libffi-dev \
       libpq-dev \
       libssl-dev \
       python3-dev \
       python3-pip \
       python3-setuptools \
       python3-venv \
       python3-wheel \
       build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && ln -nsf /usr/bin/python3.7 /usr/bin/python
     
RUN pip3 install numpy

RUN npm -g install pm2@latest 
RUN npm -g install typescript
RUN npm -g install nodemon
RUN npm -g install karma 
RUN npm -g install mocha 
RUN npm -g install chai 
RUN npm -g install cucumber
RUN npm -g install jest
RUN npm -g install enzyme
RUN npm -g install artillery --unsafe-perm=true --allow-root
RUN npm -g install selenium-webdriver
