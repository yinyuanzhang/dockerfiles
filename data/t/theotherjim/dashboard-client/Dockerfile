FROM theotherjim/node-gulp-jspm

COPY package.json /src/package.json

RUN cd /src ; npm install

COPY . /src

WORKDIR /src

RUN npm run build

EXPOSE 8080

CMD ["npm", "start"]
