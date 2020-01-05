# You should always specify a full version here to ensure all of your developers
# are running the same version of Node.
FROM node:alpine

COPY . .

RUN npm install

ENV PORT=80

# Set the command to start the node server.
CMD node index.js