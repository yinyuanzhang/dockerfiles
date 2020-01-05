FROM node:latest
LABEL maintainer "And Grin <a@grin.ly>"

ENV PORT=8080
ENV NODE_ENV=production

EXPOSE 8080
WORKDIR /app

# install npm packages in a separate layer to improve caching
COPY package*.json /app/
RUN npm set progress=false && npm install

COPY . /app

CMD [ "node", "index"]