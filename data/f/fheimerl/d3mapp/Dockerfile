FROM ubuntu:17.04

ENV appDir /var/www/app/current

RUN apt-get update

RUN apt-get install -y -q --no-install-recommends \
    apt-utils curl python python-pip \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -y autoclean

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

RUN mkdir -p /var/www/app/current
WORKDIR ${appDir}

ADD package.json ./
RUN npm install

ADD . /var/www/app/current

RUN pip install -r python-requirements.txt

EXPOSE 3000 8080

CMD ["npm", "start"]
