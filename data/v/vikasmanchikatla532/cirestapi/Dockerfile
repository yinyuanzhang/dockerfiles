FROM node
ADD data.json /code/data.json
ADD node.js /code/node.js
RUN npm install -y express
RUN npm install -y body-parser
EXPOSE 9000
CMD node /code/node.js
