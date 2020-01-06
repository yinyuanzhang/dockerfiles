FROM node:8

# Install Python 3 so we can execute our scripts on docker container

RUN apt-get -o Acquire::Check-Valid-Until=false update \
&& apt-get install -y python3-pip python3-dev \
&& cd /usr/local/bin \
&& ln -s /usr/bin/python3 python \
&& pip3 install --upgrade pip

RUN pip3 install pymongo
RUN pip3 install --no-use-pep517 pandas
RUN pip install requests

# Create app directory

WORKDIR /usr/src/app


# Install app dependencies

COPY ./package*.json ./

RUN npm install

# Bundle app source

COPY . .

CMD  [ "npm", "start" ]

EXPOSE 3000
