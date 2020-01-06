FROM node:alpine

ENV NODE_ENV production
ENV PORT 3000

WORKDIR /app
COPY . .

RUN yarn install
RUN yarn build

EXPOSE 3000
CMD ["yarn", "start"]
