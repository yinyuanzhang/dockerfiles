FROM node 
RUN mkdir -p /app/
COPY . /app
WORKDIR /app
RUN rm -rf ./node_modules
RUN npm install
EXPOSE 4000 
CMD ["node","server.js"]