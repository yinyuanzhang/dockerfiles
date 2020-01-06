FROM node:lts
ENV NODE_ENV production
WORKDIR /usr/src/app
COPY . .
RUN npm ci --production=false --silent && \
    npm run build && \
    rm -rf src && \
    npm ci --production --silent
EXPOSE 3080
CMD npm run start