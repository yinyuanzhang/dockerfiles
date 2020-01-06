FROM node:10.16-alpine

RUN mkdir -m 755 /app

COPY . /app/

WORKDIR /app

RUN yarn install --no-progress

CMD sh -c "if [ "${WATCH}" = "1" ]; then yarn test:watch; else yarn test; fi"
