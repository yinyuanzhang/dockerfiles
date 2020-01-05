FROM mhart/alpine-node:latest

WORKDIR /app
COPY . .

# If you have native dependencies, you'll need extra tools
RUN apk add --no-cache make gcc g++ python git

RUN npm install --production

EXPOSE 3000 1880
CMD ["node", "index.js"]
