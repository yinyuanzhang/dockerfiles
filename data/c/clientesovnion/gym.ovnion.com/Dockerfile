FROM node:alpine
ADD . /gym.ovnion.com/
WORKDIR /gym.ovnion.com/
RUN npm install
RUN npm install -g supervisor browserify uglifycss
RUN npm install -G envify
CMD ["npm","run","build"]
