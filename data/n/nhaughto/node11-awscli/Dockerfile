FROM node:11

RUN apt-get update

RUN apt-get install -y python3-pip

RUN apt-get install -y docker

RUN pip3 install --upgrade awscli

RUN pip3 install docker-compose

RUN npm install typescript -s -g

RUN npm install ts-node -s -g

RUN aws --version

CMD ["node"]
