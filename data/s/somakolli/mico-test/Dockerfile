FROM node

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY package.json ./
RUN npm install
RUN npm install -g @angular/cli
COPY . /usr/src/app

CMD ng serve --host 0.0.0.0
