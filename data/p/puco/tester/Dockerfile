FROM mhart/alpine-node
ADD . .
WORKDIR /server
EXPOSE 8080
RUN npm install express
CMD ["node", "index.js"]
