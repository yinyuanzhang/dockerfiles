FROM node
ENV PORT="8080"

WORKDIR /ctr-node-httpserving

COPY package.json .
RUN npm install 

COPY . .

EXPOSE ${PORT}

ENTRYPOINT [ "npm", "start", "--" ]
CMD ["--file", "example/data.json", "--headers", "Content-Type: application/json"]
