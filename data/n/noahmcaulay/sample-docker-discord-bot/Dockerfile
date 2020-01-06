FROM node:latest

# Create the directory
RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot

# Copy and install the bot
COPY package.json /usr/src/bot
RUN npm install

# Yasss
COPY . /usr/src/bot

# Start the bot
CMD ["node", "index.js"]
