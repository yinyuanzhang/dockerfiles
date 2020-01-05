FROM node
ENV PORT="8080"

WORKDIR /ctr-node-httpapp

COPY package.json .
RUN npm install 

COPY . .

EXPOSE ${PORT}
ENTRYPOINT [ "npm", "start" ]
