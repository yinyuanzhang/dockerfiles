FROM node:alpine
ADD . /pizzeriadieguito.com.ar/
WORKDIR /pizzeriadieguito.com.ar/
RUN npm install
RUN npm install -g supervisor browserify uglifycss
RUN npm install -G envify
CMD ["npm","run","build"]
