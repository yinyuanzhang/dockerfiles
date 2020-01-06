FROM node
EXPOSE 8080
CMD node server.js
COPY package.json .
RUN npm i
# COPY app /app
# COPY public /public
COPY . .