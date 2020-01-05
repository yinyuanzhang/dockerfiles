FROM node:carbon-jessie

ARG POLYFILL_VERSION=v3.25.0
WORKDIR /app
RUN wget -c https://github.com/Financial-Times/polyfill-service/archive/${POLYFILL_VERSION}.tar.gz -O - | tar --strip-components=1 -xz
ENV NODE_ENV production

RUN npm i --production
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
