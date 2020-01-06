FROM node:9.6.1

RUN mkdir /usr/src/siriporn-resume
WORKDIR /usr/src/siriporn-resume

COPY package.json /usr/src/siriporn-resume/
RUN npm install

COPY . /usr/src/siriporn-resume

CMD ["npm","start"]

