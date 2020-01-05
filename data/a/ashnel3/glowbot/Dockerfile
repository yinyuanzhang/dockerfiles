FROM node:12.13.1

# ENV
ENV NODE_ENV=production

# Make project folder
RUN mkdir -p /usr/src/glowbot
RUN chown -R node: /usr/src/glowbot
WORKDIR /usr/src/glowbot

# Install bot
COPY package* ./
RUN npm i --no-optional

COPY . /usr/src/glowbot

# Switch to limited user
USER node

# Start
CMD ["node", "dist/index.js"]
