FROM node:6
MAINTAINER jowilkey@cisco.com

WORKDIR /app

ADD .git .
ADD src/api/ .

RUN npm install -d && \
    npm run build && \
    npm test && \
    npm prune --production

# Cleanup
RUN rm -rf .git

EXPOSE 3000

CMD ["npm", "start"]
