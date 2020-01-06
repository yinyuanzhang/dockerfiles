FROM node:8.1.0-alpine

# use nodemon for development
#RUN npm install --global nodemon

#RUN mkdir -p /home/nodejs/app/server 
#ADD . /home/nodejs/app/server 

#WORKDIR /home/nodejs/app/server


#COPY package.json .
#RUN npm install --quiet

#COPY . .

# Run nodemon
#CMD ["npm", "start"]



RUN mkdir /server

RUN npm install nodemon -g
RUN npm install -g jasmine-node


ADD ./server /server
WORKDIR /server
RUN npm install

#ADD server/nodemon.json /server/nodemon.json

EXPOSE 3000

CMD npm start