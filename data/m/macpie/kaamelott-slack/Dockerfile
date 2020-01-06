FROM node:8

WORKDIR /tmp
RUN git clone https://github.com/2ec0b4/kaamelott-soundboard.git

RUN mkdir -p /opt/kaamelott
WORKDIR /opt/kaamelott

RUN cp -R /tmp/kaamelott-soundboard/sounds /opt/kaamelott/sounds

ADD package.json package.json
RUN npm install

ADD app app
ADD index.js index.js

CMD ["npm", "start"]
